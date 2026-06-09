pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                sh 'docker build -t flask-demo:v1 .'
            }
        }

        stage('Push') {
            steps {
                sh 'docker push registry.odc.sunline.cn/demo/flask-demo:v1'
            }
        }

        stage('Deploy') {
            steps {
                sh 'helm upgrade --install flask-demo ./flask-demo'
            }
        }

    }

}