from flask import Flask, request
from ultralytics import YOLO
import cv2, requests, threading, time

app = Flask(__name__)
model = YOLO("yolov8n.pt")     
BACKEND = "http://localhost:8080"
workers = {}                       # camera_id -> stop Event


def send_heartbeat(cam_id, status):
    try:
        requests.post(f"{BACKEND}/api/cameras/heartbeat",
                      json={"cameraId": cam_id, "status": status}, timeout=3)
    except requests.RequestException:
        pass


def monitor(cam, stop):
    cap = cv2.VideoCapture(cam["streamUrl"])
    last_alert, last_status = 0, None
    while not stop.is_set():
        ok, frame = cap.read()
        status = "ONLINE" if ok else "OFFLINE"
        if status != last_status:
            send_heartbeat(cam["id"], status)
            last_status = status
        if not ok:                                  
            time.sleep(2)
            cap.release()
            cap = cv2.VideoCapture(cam["streamUrl"])
            continue

        result = model(frame, classes=[0], conf=0.5, verbose=False)[0]   # 0 = person
        count = len(result.boxes)
        if count > 0 and time.time() - last_alert > 30:                  # 30s cooldown
            try:
                requests.post(f"{BACKEND}/api/alerts", json={
                    "alertType": "INTRUDER",
                    "severity": "CRITICAL",
                    "message": f"{count} person(s) detected",
                    "camera": {"id": cam["id"]}}, timeout=3)
                last_alert = time.time()
            except requests.RequestException as e:
                print("Alert send failed:", e)
        time.sleep(0.2)                              # ~5 frames/sec
    cap.release()


def start_worker(cam):
    if cam["id"] in workers:
        workers[cam["id"]].set()                    
    stop = threading.Event()
    workers[cam["id"]] = stop
    threading.Thread(target=monitor, args=(cam, stop), daemon=True).start()


@app.route("/register-camera", methods=["POST"])
def register_camera():
    start_worker(request.json)
    return {"status": "success", "message": "Camera monitoring started"}


@app.route("/remove-camera/<int:cam_id>", methods=["DELETE"])
def remove_camera(cam_id):
    if cam_id in workers:
        workers.pop(cam_id).set()
    return {"status": "removed"}


@app.route("/health")
def health():
    return {"status": "online", "cameras_monitored": len(workers)}


def resume_cameras():
    """Flask restart ho to DB ke saare cameras ki monitoring dobara shuru."""
    try:
        for cam in requests.get(f"{BACKEND}/api/cameras", timeout=5).json():
            start_worker(cam)
    except Exception as e:
        print("Could not load cameras:", e)


if __name__ == "__main__":
    resume_cameras()
    app.run(port=5000)
