# DevOps Final Project

**Name:** Syeda Zunaira  
**Registration Number:** 2312305  

## Project Overview
This is a containerised microservice application demonstrating a complete DevOps toolchain, including Docker, GitHub Actions for CI/CD, and deployment on AWS EC2.

## Architecture Description
The application consists of two main components:
1. **Flask Web Application**: A REST API providing endpoints for adding students, retrieving students, and checking the health of the service.
2. **PostgreSQL Database**: A relational database to store the student records persistently. The data is saved in a Docker volume so it is not lost when containers restart.

These components are orchestrated using Docker Compose.

## Setup Instructions (Running Locally)

To run this project locally, you need to have Docker and Docker Compose installed.

1. Clone this repository.
2. Open a terminal in the project directory.
3. Run the following command:
   ```bash
   docker-compose up -d --build
   ```
4. Access the API at `http://localhost:8000/health`.

## CI/CD and Cloud Deployment
- Every push to the `main` branch triggers a GitHub Actions pipeline.
- The pipeline checks the code and automatically deploys the latest version to an AWS EC2 instance.
