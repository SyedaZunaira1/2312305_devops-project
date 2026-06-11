# DevOps Project - Student Registration System

**Name:** Syeda Zunaira  
**Registration Number:** 2312305  

## Project Overview

This is a containerized FastAPI application with a PostgreSQL backend, designed as part of the DevOps Fundamentals final project. It features automated CI/CD pipelines via GitHub Actions and deploys to an AWS EC2 instance using Docker Compose.

## Architecture

- **Web Service:** FastAPI + Uvicorn exposing REST API on port 8000
- **Database:** PostgreSQL 15 running in a container with persistent named volumes
- **CI Pipeline:** GitHub Actions runs `flake8` linting and `pytest` on every push/PR
- **CD Pipeline:** GitHub Actions automatically deploys to the AWS EC2 instance on push to the `main` branch
- **Cloud Server:** AWS EC2 (Ubuntu) running Docker & Docker Compose

## Setup Instructions

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/SyedaZunaira1/2312305_devops-project.git
   cd 2312305_devops-project
   ```

2. Copy the `.env.example` to `.env` and fill in the database credentials:
   ```bash
   cp .env.example .env
   ```

3. Run with Docker Compose:
   ```bash
   docker compose up --build
   ```

4. The API will be available at `http://localhost:8000`. You can visit `http://localhost:8000/docs` for the interactive Swagger UI.

### Production Deployment (EC2)

The application automatically deploys to an AWS EC2 instance when changes are pushed to the `main` branch. 
The GitHub Actions workflow connects via SSH, pulls the latest code, creates the `.env` file using GitHub Secrets, and starts the services using `docker-compose.prod.yml`.
