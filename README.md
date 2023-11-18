# Social Media Challenge

Welcome to the Social Media Challenge repository! This project is a simple web application built with Django, designed to create posts for different users (A social media app*).

## Background

Our infrastructure consists of a mix of local and cloud-deployed resources, primarily using Google Cloud and Amazon Web Services. We utilize a combination of virtual machines and containerized services. The stack is dominated by open-source tools and frameworks, with a Linux-based server fleet, a preference for Ubuntu/Debian, and deployment automation through Ansible.

The majority of our systems are implemented in Python and Go. Our CI/CD pipeline relies on a self-hosted Gitlab instance and Gitlab CI. Monitoring is achieved using StatsD and Grafana, and PostgreSQL serves as our primary database, with occasional usage of Oracle or SQL Server when interacting with clients’ systems. We expose REST and GraphQL APIs, consumed by single-page frontend apps and mobile apps. NGINX reverse proxies typically secure these APIs, except for Go services, which may be exposed directly.

## Challenge

The challenge is to fix and optimize the project.

There are areas where improvements and fixes can be made that you need to figure out.

Bonus: Add tests to your the final implementation

## Getting Started

Follow these steps to get the project up and running on your local machine:

1. **Fork** and Clone the repository:

2. Install the project dependencies:

3. Apply database migrations:

4. Run the development server:

5. Visit `http://127.0.0.1:8000/social_media/home/` in your web browser. You should see the below if successful.

![Alt text](<Screenshot from 2023-11-18 10-54-28.png>)

## How to Contribute

In your **forked** repository, Create a Pull request with the changes you have made.

Checklist:

- Fix bugs, if any
- Optimize workflows, if need be
- Use PostgreSQL 13+ as the DB
- Dockerize the project

## Optimization and Deployment Challenge

The main challenge is to optimize the project and fix any issues you find. Additionally, your goal is to deploy the project to a cloud provider of your choice using Ansible. Pay close attention to:

- **Security / Hardening**
- **Database optimization**
- **Monitoring / Observability**
- **Scalability / Failover**
- **Backup & Disaster Recovery**

### Deployment Steps

1. Include step-by-step instructions for deploying the project to your chosen cloud provider

2. Provide any necessary configuration files or settings for deployment.

3. Optional: Include a sample configuration file for environment variables.

## Documentation

Document your setup thoroughly. The technical interview will be based on the configuration management and corresponding documentation.

Once done, share (a) link(s) to your changes for review

## Timeline

This information will be shared by your recruiter
