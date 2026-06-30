pipeline {
    agent any

    environment {
        // Define your staging environment deployment path or target
        STAGING_DIR = "/var/www/flask-staging"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to staging environment...'
                // Simple staging mock deployment deployment execution
                sh "mkdir -p ${STAGING_DIR} && cp -R * ${STAGING_DIR}/"
            }
        }
    }

    post {
        success {
            mail to: 'your-email@example.com',
                 subject: "SUCCESS: Jenkins Build Notification: ${currentBuild.fullDisplayName}",
                 body: "The pipeline executed successfully! Check details at: ${env.BUILD_URL}"
        }
        failure {
            mail to: 'your-email@example.com',
                 subject: "FAILURE: Jenkins Build Notification: ${currentBuild.fullDisplayName}",
                 body: "The pipeline failed during execution. Check logs at: ${env.BUILD_URL}"
        }
    }
}
