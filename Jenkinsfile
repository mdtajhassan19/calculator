pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start API') {
            steps {
                bat 'start /B uvicorn app.main:app --host 0.0.0.0 --port 8000'
                timeout(time: 10, unit: 'SECONDS') {}
            }
        }

        stage('Run Postman Tests') {
            steps {
                bat '''
                newman run tests/calculator.postman_collection.json ^
                -e tests/env.json ^
                -r cli,html ^
                --reporter-html-export report.html
                '''
            }
        }
    }
}