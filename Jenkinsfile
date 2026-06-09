pipeline {

    agent any

    stages {

        stage('Build') {

            steps {
                bat 'docker build -t flask-demo:v1 .'
            }

        }

        stage('Push') {

            steps {
                bat 'docker push registry.odc.sunline.cn/demo/flask-demo:v1'
            }

        }

        stage('Deploy') {

            steps {
                bat 'helm upgrade --install flask-demo ./flask-demo'
            }

        }

    }

}