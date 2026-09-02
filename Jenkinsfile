pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the latest source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies and preparing the application...'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated unit tests...'
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Package') {
            steps {
                echo 'Creating the deployment artifact...'
                sh 'python3 package.py'
            }
        }

        stage('Deploy to Test') {
            steps {
                echo 'Deploying the packaged application to the test environment...'
                sh 'mkdir -p test-environment'
                sh 'cp deployment/jenkins-cicd-app.zip test-environment/'
                sh 'ls -la test-environment/'
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the console output to identify the problem.'
        }
        always {
            archiveArtifacts artifacts: 'deployment/*.zip', allowEmptyArchive: true
        }
    }
}
