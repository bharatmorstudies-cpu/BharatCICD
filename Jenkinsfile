pipeline {
    agent any

    environment {
        PYTHONPATH = '.'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh './venv/bin/pytest'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application to Staging Environment...'
                // Mock deployment script
                sh 'echo "Application successfully deployed to staging!"'
            }
        }
    }
    
    post {
        success {
            echo 'Build Succeeded! Sending email notification...'
            // Optional: mail to: 'admin@example.com', subject: 'Success'
        }
        failure {
            echo 'Build Failed! Sending alert notification...'
            // Optional: mail to: 'admin@example.com', subject: 'Failure'
        }
    }
}
