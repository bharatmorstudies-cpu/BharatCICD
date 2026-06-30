pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies globally for Jenkins user...'
                // --break-system-packages bypasses Debian's managed environment lock in pipeline scripts
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests with Pytest...'
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application to Staging Environment...'
            }
        }
    }

    post {
        always {
            echo "Execution complete."
        }
        failure {
            echo "Build Failed! Sending alert notification..."
        }
    }
}
