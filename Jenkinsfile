pipeline {
    agent any

    stages {

        stage('Docker Check') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t flask-demo:v1 .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push registry.odc.sunline.cn/demo/flask-demo:v1'
            }
        }

        stage('Helm Check') {
            steps {
                sh 'helm version'
            }
        }
    }
}