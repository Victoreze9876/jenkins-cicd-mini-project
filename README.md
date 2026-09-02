# Jenkins CI/CD Pipeline Mini Project

## Project Overview

This project demonstrates the implementation of a basic Continuous Integration and Continuous Delivery (CI/CD) pipeline using Jenkins, GitHub and Python.

The application is a simple Python calculator. The application itself was intentionally kept small because the main purpose of the project was to understand how Jenkins can automate the different stages of a software delivery process.

The pipeline automatically checks out the source code, prepares the application, runs automated tests, creates a deployment artifact and performs a basic deployment to a test environment.

## Technologies Used

* Jenkins
* Git
* GitHub
* Python 3
* Python unittest
* Java / OpenJDK 21
* Homebrew
* macOS
* Jenkins Declarative Pipeline

## Project Structure

```text
jenkins-cicd-mini-project/
├── src/
│   ├── __init__.py
│   └── app.py
├── tests/
│   └── test_app.py
├── Jenkinsfile
├── package.py
├── requirements.txt
├── README.md
└── .gitignore
```

## CI/CD Pipeline

The Jenkins pipeline is defined as code inside the `Jenkinsfile` stored in this repository.

The pipeline follows this process:

```text
GitHub Repository
       ↓
    Jenkins
       ↓
    Checkout
       ↓
     Build
       ↓
      Test
       ↓
    Package
       ↓
Deploy to Test
```

### 1. Checkout

Jenkins retrieves the latest version of the application from the GitHub repository.

### 2. Build

The Build stage prepares the Python application and handles the required dependencies.

### 3. Test

Automated unit tests are executed using Python's built-in `unittest` framework.

Five automated tests check:

* Addition
* Subtraction
* Multiplication
* Division
* Division by zero

A failing test causes the Jenkins pipeline to fail, providing immediate feedback about a potential problem.

### 4. Package

After the tests pass, the application is packaged into a ZIP artifact.

The generated artifact is:

`deployment/jenkins-cicd-app.zip`

### 5. Deploy to Test

The packaged application is copied into a test environment.

This provides a simple demonstration of how a successfully tested application can automatically move to the deployment stage.

## Automatic Build Trigger

Jenkins was configured using Poll SCM to check the GitHub repository for new commits.

The polling schedule used was:

```text
H/2 * * * *
```

To test the automation, I made a change to the project, committed it and pushed it to GitHub.

Jenkins detected the repository change and automatically started the pipeline without requiring me to manually select Build Now.

## Running the Tests Locally

The automated tests can also be executed locally using:

```bash
python3 -m unittest discover -s tests -v
```

A successful test execution should finish with:

```text
Ran 5 tests

OK
```

The application can be run using:

```bash
python3 src/app.py
```

## Troubleshooting Exercise

As part of the project, I deliberately introduced an incorrect unit test.

The addition test was temporarily changed to expect `2 + 3` to equal `6`.

After the change was pushed to GitHub, Jenkins automatically detected the commit and started a new pipeline. The Test stage failed.

I reviewed the Jenkins Console Output and identified the incorrect expected value.

I then corrected the test, ran the tests locally and confirmed that all five tests passed. The correction was committed and pushed to GitHub.

Jenkins automatically executed another pipeline, which completed successfully.

This exercise demonstrated how Jenkins can provide fast feedback and how pipeline logs can be used to diagnose and resolve build problems.

## Jenkins Plugins

The Jenkins installation used the recommended plugins provided during the initial setup.

The main functionality required for this project included:

* Git plugin
* Pipeline functionality
* Pipeline: SCM Step

These allowed Jenkins to retrieve source code from Git and execute the pipeline stored in the Jenkinsfile.

## Security

No passwords, API keys or other sensitive credentials are stored directly inside the Jenkinsfile or GitHub repository.

In a production environment, sensitive information should be managed using Jenkins Credentials and referenced securely from the pipeline.

## What I Learned

Completing this project gave me practical experience with the main components of a basic CI/CD workflow.

I learned how Git and GitHub are used to manage source code while Jenkins can automate processes that would otherwise have to be performed manually.

I also gained practical experience with Pipeline-as-Code by storing the Jenkins pipeline configuration in a Jenkinsfile alongside the application.

The troubleshooting exercise helped me understand the importance of automated testing and Jenkins Console Output. A code or test problem can be detected automatically, investigated through the logs and corrected before proceeding further through the delivery process.

## Conclusion

The project successfully demonstrates a basic Jenkins CI/CD pipeline.

The final pipeline can:

* Retrieve source code from GitHub
* Prepare the Python application
* Execute automated unit tests
* Stop when tests fail
* Package the application
* Perform a basic deployment
* Detect new GitHub commits automatically
* Provide logs for troubleshooting failed builds

Overall, this project helped me move from understanding CI/CD as a theoretical concept to seeing how GitHub, automated testing and Jenkins work together in practice.
