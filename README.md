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
