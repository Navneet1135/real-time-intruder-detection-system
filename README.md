# Real-Time Intruder Detection System

A full-stack security monitoring application designed to manage cameras, monitor security status, and handle alerts through a web-based dashboard.

## Overview

The **Real-Time Intruder Detection System** combines a React-based frontend, Spring Boot backend, Python Flask service, and MySQL database to provide a centralized platform for security monitoring.

The application includes user authentication, camera management, monitoring workflows, and alert management through REST-based communication between the frontend and backend services.

## Features

* 🔐 **User Authentication** — Registration and login functionality.
* 📹 **Camera Management** — Add and manage registered cameras.
* 🚨 **Alert Management** — View and manage security alerts.
* 📊 **Monitoring Dashboard** — Centralized interface for camera and alert information.
* 🔄 **Backend APIs** — REST APIs for authentication, cameras, alerts, and related operations.
* 🐍 **Python Service** — Flask-based service for supporting monitoring workflows.
* 🗄️ **Database Integration** — MySQL-based persistence for application data.
* 🛡️ **Spring Security** — Backend security configuration for protected application functionality.

## System Architecture

```text
                    ┌─────────────────────┐
                    │    React Frontend   │
                    │      Vite + JS      │
                    └──────────┬──────────┘
                               │
                         REST API Calls
                               │
                    ┌──────────▼──────────┐
                    │   Spring Boot API   │
                    │   Java + Security   │
                    └───────┬───────┬─────┘
                            │       │
                       MySQL DB     │
                            │       │
                    ┌───────▼───┐   │
                    │   Data    │   │
                    │Persistence│   │
                    └───────────┘   │
                                    │
                           ┌────────▼────────┐
                           │  Python Flask   │
                           │     Service     │
                           └─────────────────┘
```

## Tech Stack

### Frontend

* React.js
* Vite
* JavaScript
* CSS

### Backend

* Java
* Spring Boot
* Spring Security
* Spring Data JPA
* REST APIs
* Maven

### Python Service

* Python
* Flask

### Database

* MySQL

### Development Tools

* Git
* GitHub
* VS Code
* Maven

## Project Structure

```text
real-time-intruder-detection-system/
│
├── cctvBackend/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   └── cctv_backend/
│   │   │   │       └── demo/
│   │   │   │           ├── config/
│   │   │   │           ├── controller/
│   │   │   │           ├── dto/
│   │   │   │           ├── entity/
│   │   │   │           ├── repository/
│   │   │   │           └── service/
│   │   │   └── resources/
│   │   └── test/
│   ├── pom.xml
│   ├── mvnw
│   └── mvnw.cmd
│
├── frontend/
│   └── frontend/
│       ├── src/
│       │   ├── components/
│       │   ├── pages/
│       │   └── services/
│       ├── public/
│       ├── package.json
│       └── vite.config.js
│
├── python/
│   └── server.py
│
├── .gitignore
└── README.md
```

## Backend Modules

The Spring Boot backend is organized into separate layers:

* **Controllers** — Handle HTTP requests and expose REST endpoints.
* **Services** — Contain application/business logic.
* **Repositories** — Handle database operations.
* **Entities** — Represent application data models.
* **DTOs** — Handle structured request data.
* **Security Configuration** — Manages backend security configuration.

## Frontend

The React application provides:

* Login and registration pages
* Dashboard
* Camera management interface
* Alert table
* Navigation components
* API service layer for backend communication

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Navneet1135/real-time-intruder-detection-system.git

cd real-time-intruder-detection-system
```

### 2. Configure MySQL

Create a MySQL database and update the database configuration in:

```text
cctvBackend/src/main/resources/application.properties
```

Use your local MySQL username, password, and database name.

> Do not commit real database passwords or other credentials to GitHub.

### 3. Run the Spring Boot Backend

Navigate to:

```bash
cd cctvBackend
```

Run:

```bash
./mvnw spring-boot:run
```

On Windows:

```powershell
.\mvnw.cmd spring-boot:run
```

### 4. Run the React Frontend

Open another terminal:

```bash
cd frontend/frontend
npm install
npm run dev
```

The Vite development server will provide the local frontend URL.

### 5. Run the Python Service

Open another terminal:

```bash
cd python
pip install flask
python server.py
```

## API Components

The backend contains REST controllers for major application modules including:

* Authentication
* Camera management
* Alert management

The frontend communicates with these backend services through the API service layer.

## Future Improvements

* Real-time CCTV video streaming
* Advanced intrusion detection using computer vision
* Object and person detection
* Real-time notifications
* Multi-camera monitoring
* Role-based access control
* Cloud deployment
* Improved monitoring analytics

## Author

**Navneet Pal**

B.Tech Computer Science Engineering
Oriental Institute of Science and Technology

GitHub: [Navneet1135](https://github.com/Navneet1135)

---

## License

This project is intended for educational and development purposes.
