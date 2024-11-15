# Flask AWS Load Balancer

This project is a containerized Flask web application that is automatically deployed to AWS using GitHub Actions. The deployment involves creating two EC2 instances, setting up a load balancer, and running the application on AWS. The web app displays the user's browser agent information.

## Project Overview

The repository contains the following key components:

- **Dockerfile**: Defines the Docker container for the Flask application.
- **app.py**: The main application file for the Flask server.
- **main.tf**: Terraform configuration file for deploying resources to AWS.
- **GitHub Actions Workflow**: Automated CI/CD pipeline to build and deploy the Docker container to AWS.
- **Templates**: Directory containing `index.html` with a simple UI for the Flask app.

## Features

- **Automated Deployment**: Uses GitHub Actions to build the Docker image and deploy it to AWS.
- **Load Balancer**: Configured with AWS to manage traffic between two EC2 instances.
- **Flask App**: A simple Flask application that shows the user's browser agent.

## Repository Structure

```plaintext
.github/workflows/       # Contains the GitHub Actions workflow file for deployment
templates/               # Contains HTML templates for the Flask application
Dockerfile               # Docker configuration for building the container image
app.py                   # Main application file for the Flask app
main.tf                  # Terraform configuration for AWS resources
requirements.txt         # Python dependencies for the Flask app
```
## Getting Started

### Prerequisites

- Docker
- Terraform
- AWS Account and credentials
- GitHub repository with Actions enabled

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Shift-Happens/Flask_AWS_load_balacer.git
    cd Flask_AWS_load_balacer
    ```

2. Update AWS credentials in your GitHub repository secrets (if not done already):
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

3. Customize any necessary variables in `main.tf` for your AWS setup.

4. Push a commit to trigger the GitHub Actions workflow.

### Usage

The application is deployed to AWS automatically on commit. You can access it via the AWS Load Balancer DNS name once the deployment is complete.

## Workflow

1. On each commit, GitHub Actions will:
   - Build the Docker image for the Flask app.
   - Deploy it to AWS using Terraform.
   - Create two EC2 instances and set up a load balancer to distribute the load.

2. The Flask application displays the user agent information of visitors.

