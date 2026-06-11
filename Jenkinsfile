pipeline {

    agent any

    options {
        timestamps()
    }

    environment {
        REGISTRY         = "registry.odc.sunline.cn"
        IMAGE_REPOSITORY = "${REGISTRY}/demo/flask-demo"
        IMAGE_TAG        = "${BUILD_NUMBER}"

        NAMESPACE        = "justine-sandbox"
        RELEASE_NAME     = "flask-demo"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image ${IMAGE_REPOSITORY}:${IMAGE_TAG}"

                sh """
                    docker build \
                    -t ${IMAGE_REPOSITORY}:${IMAGE_TAG} .
                """
            }
        }

        stage('Login to Registry') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'odc-registry',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {

                    sh '''
                        echo "$DOCKER_PASS" | \
                        docker login registry.odc.sunline.cn \
                        -u "$DOCKER_USER" \
                        --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing image to Harbor registry"

                sh """
                    docker push ${IMAGE_REPOSITORY}:${IMAGE_TAG}
                """
            }
        }

        stage('Verify Build Environment') {
            steps {
                sh '''
                    docker --version
                    helm version
                    kubectl version --client
                '''
            }
        }

        stage('Deploy to Rancher Kubernetes') {
            steps {
                withCredentials([
                    file(
                        credentialsId: 'rancher-kubeconfig',
                        variable: 'KUBECONFIG_FILE'
                    )
                ]) {

                    sh """
                        export KUBECONFIG=\$KUBECONFIG_FILE

                        helm upgrade --install ${RELEASE_NAME} . \
                          --namespace ${NAMESPACE} \
                          --set image.repository=${IMAGE_REPOSITORY} \
                          --set image.tag=${IMAGE_TAG} \
                          --wait \
                          --timeout 5m
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

                        echo "===== Pods ====="
                        kubectl get pods -n ${NAMESPACE}

                        echo "===== Deployments ====="
                        kubectl get deployments -n ${NAMESPACE}

                        echo "===== Services ====="
                        kubectl get services -n ${NAMESPACE}

                        echo "===== Rollout Status ====="
                        kubectl rollout status deployment/${RELEASE_NAME} \
                          -n ${NAMESPACE} \
                          --timeout=300s
                    """
                }
            }
        }
    }

    post {

        success {
            echo """
==================================================
 Deployment Successful
==================================================
Image:
${IMAGE_REPOSITORY}:${IMAGE_TAG}

Namespace:
${NAMESPACE}

Release:
${RELEASE_NAME}
==================================================
"""
        }

        failure {
            echo """
==================================================
 Deployment Failed
Check Jenkins console logs for details.
==================================================
"""
        }

        always {
            sh '''
                docker image prune -f || true
            '''
        }
    }
}