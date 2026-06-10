pipeline {
    agent any

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t registry.odc.sunline.cn/demo/flask-demo:v2 .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'odc-registry',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login registry.odc.sunline.cn \
                    -u "$DOCKER_USER" --password-stdin
                    '''
                }
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