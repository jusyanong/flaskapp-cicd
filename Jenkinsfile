pipeline {

    agent any

    stages {

        stage('Docker Check') {
            steps {
                sh 'docker --version'
                sh 'docker ps'
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

        stage('Deploy') {
            steps {
                sh 'helm upgrade --install flask-demo .'
            }
        }

    }

}