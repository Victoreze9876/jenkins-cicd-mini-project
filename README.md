# Jenkins CI/CD Mini Project

## Project Overview

This mini project demonstrates a basic Continuous Integration and Continuous Delivery pipeline using Jenkins and GitHub.

The application is a small Python calculator. The application itself is intentionally simple so that the focus remains on understanding the Jenkins CI/CD process.

## Pipeline Flow

1. Checkout - Jenkins retrieves the latest code from Git.
2. Build - Python dependencies are installed and the project is prepared.
3. Test - Automated unit tests are executed.
4. Package - The application is packaged into a ZIP artifact.
5. Deploy to Test - The artifact is copied to a test-environment directory.

## Technologies Used

- Python
- Jenkins
- Git
- GitHub
- Jenkins Declarative Pipeline

## Expected Result

A successful Jenkins run should show all pipeline stages as successful. The generated artifact is:

`deployment/jenkins-cicd-app.zip`

## Notes
Automatic Jenkins trigger test completed.
This project does not require third-party Python packages. Python's built-in `unittest` framework is used for testing.
