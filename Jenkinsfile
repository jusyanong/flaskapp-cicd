pipeline {
    agent any

    environment {
        IMAGE_NAME = "registry.odc.sunline.cn/demo/flask-demo"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build Image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
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
                sh """
                docker push ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('Tools Check') {
            steps {
                sh 'docker --version'
                sh 'helm version'
                sh 'kubectl version --client'
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([
                    file(
                        credentialsId: 'rancher-kubeconfig',
                        variable: 'KUBECONFIG_FILE'
                    )
                ]) {
                    sh """
                    export KUBECONFIG=\$KUBECONFIG_FILE

                    helm upgrade --install flask-demo . \
                      --set image.repository=${IMAGE_NAME} \
                      --set image.tag=${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                withCredentials([
                    file(
                        credentialsId: 'rancher-kubeconfig',
                        variable: 'KUBECONFIG_FILE'
                    )
                ]) {
                    sh """
                    export KUBECONFIG=\$KUBECONFIG_FILE

                    kubectl get pods
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}