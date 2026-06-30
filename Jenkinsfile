pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies using pip globally...'
                sh 'pip install --break-system-packages -r requirements.txt || pip install -r requirements.txt || python3 -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests using pytest...'
                sh 'pytest || python3 -m pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application to staging environment...'
            }
        }
    }
    post {
        success {
            echo 'Build Succeeded!'
        }
        failure {
            echo 'Build Failed! Sending alert notification...'
        }
    }
}
