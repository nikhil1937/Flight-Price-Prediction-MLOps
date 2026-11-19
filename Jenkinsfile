
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub'
                checkout scm
            }
        }

        stage('Verify Source') {
            steps {
                echo 'Verifying project files'

                script {
                    if (!fileExists('requirements.txt')) {
                        error 'requirements.txt not found!'
                    }

                    if (!fileExists('app.py')) {
                        error 'app.py not found!'
                    }
                }

                echo 'Project files verified successfully'
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\Ashish\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" --version'

                bat '"C:\\Users\\Ashish\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Ashish\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv .venv'

                bat '.venv\\Scripts\\python -m pip install --upgrade pip'

                bat '.venv\\Scripts\\python -m pip install -r requirements.txt'
            }
        }
    }
}
