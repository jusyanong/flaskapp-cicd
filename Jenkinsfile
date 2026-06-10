pipeline {
agent any


environment {
    IMAGE_NAME = "registry.odc.sunline.cn/demo/flask-demo"
    IMAGE_TAG = "${BUILD_NUMBER}"
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

    stage('Helm Check') {
        steps {
            sh 'helm version'
        }
    }

    stage('Deploy') {
        steps {
            sh """
            helm upgrade --install flask-demo . \
            --set image.repository=${IMAGE_NAME} \
            --set image.tag=${IMAGE_TAG}
            """
        }
    }
}


}
