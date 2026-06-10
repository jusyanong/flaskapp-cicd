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
                sh 'docker build -t registry.odc.sunline.cn/demo/flask-demo:v2 .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push registry.odc.sunline.cn/demo/flask-demo:v2'
            }
        }

        stage('Helm Check') {
            steps {
                sh 'helm version'
            }
        }
    }
}