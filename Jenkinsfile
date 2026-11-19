
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
                    def requiredFiles = [
                        'requirements.txt',
                        'app.py',
                        'test_model.py',
                        'test_data.csv',
                        'flight_price_model.keras',
                        'preprocessor.pkl'
                    ]

                    for (file in requiredFiles) {
                        if (!fileExists(file)) {
                            error "${file} not found!"
                        }
                    }
                }

                echo 'All required project files verified'
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

        stage('Automated Model Testing') {
            steps {
                echo 'Running automated model tests'

                bat '.venv\\Scripts\\python -m pytest -v test_model.py'
            }
        }
    }
}
