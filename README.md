# FastAPI Starter by Akaday

## Overview
**FastAPI Starter by Akaday** is a template designed to kickstart FastAPI projects quickly and efficiently. This template provides a solid foundation with essential features and configurations, making it easier to develop robust and scalable FastAPI applications.

## Features
- **FastAPI Setup**: A basic setup to get started with FastAPI.
- **Docker Support**: Pre-configured Dockerfile for containerization.
- **GitHub Actions**: Automated workflows for building and deploying Docker images.
- **Modular Structure**: Organized project structure to maintain code clarity and ease of development.

## Project Structure
```plaintext
fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints/
│   │       └── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py
├── requirements.txt
├── Dockerfile
├── .env
├── .gitignore
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.7+
- FastAPI
- Uvicorn
- Docker (optional, for containerization)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/akaday/FastAPI-Starter.git
    cd FastAPI-Starter
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Authentication and Validation Setup
1. Install additional dependencies:
    ```sh
    pip install passlib[bcrypt] python-jose pydantic
    ```

2. Update the `requirements.txt` file to include these dependencies:
    ```plaintext
    fastapi
    uvicorn
    passlib[bcrypt]
    python-jose
    pydantic
    ```

### Running the Application
1. Start the FastAPI application:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to see the welcome message.

### Usage Instructions

#### User Registration
To create a new user, send a POST request to `/users/` with the following JSON body:
```json
{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "password": "yourpassword"
}
```

#### User Login
To log in and get an access token, send a POST request to `/token` with the following form data:
```plaintext
username: johndoe@example.com
password: yourpassword
```

#### Get Current User
To get the current authenticated user, send a GET request to `/users/me` with the `Authorization` header:
```plaintext
Authorization: Bearer <access_token>
```

## Deployment
Consider deploying your app using services like Heroku, AWS, or Azure. Here are some basic steps for deploying with Docker:

1. Build the Docker image:
    ```sh
    docker build -t fastapi-starter .
    ```

2. Run the Docker container:
    ```sh
    docker run -d -p 8000:8000 fastapi-starter
    ```

3. Open your browser and navigate to `http://127.0.0.1:8000` to see the welcome message.
