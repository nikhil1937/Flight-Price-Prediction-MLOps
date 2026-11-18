
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
                script {
                    if (isUnix()) {
                        sh 'python3 --version'
                        sh 'python3 -m pip --version'
                    } else {
                        bat 'python --version'
                        bat 'python -m pip --version'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m venv .venv'
                        sh '.venv/bin/python -m pip install --upgrade pip'
                        sh '.venv/bin/python -m pip install -r requirements.txt'
                    } else {
                        bat 'python -m venv .venv'
                        bat '.venv\\Scripts\\python -m pip install --upgrade pip'
                        bat '.venv\\Scripts\\python -m pip install -r requirements.txt'
                    }
                }
            }
        }
    }
}
