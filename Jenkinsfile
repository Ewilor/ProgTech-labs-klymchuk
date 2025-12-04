pipeline {
  options { timestamps()  }
  agent none
  stages {
    stage('Check scm') {
      agent any
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        echo "Building...${BUILD_NUMBER}"
        echo 'Build complete'
      }
    }
    stage('Test') {
      agent {
        docker {
          image 'python:3.9-alpine'
          args '-u root'
        }
      }
      steps {
        sh 'apk add --no-cache build-base'
        sh 'pip install xmlrunner'
        sh 'python3 tests.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
        success {
          echo 'Tests passed!'
        }
        failure {
          echo 'Tests failed!'
        }
      }
    }
    stage('Package and Push') {
      agent any 
      steps {
        script {
          def DOCKER_HUB_USERNAME = "bohdank15" 
          def IMAGE_NAME = "${DOCKER_HUB_USERNAME}/progtech-klymchuk"
          
          def DOCKER_IMAGE_TAGGED = "${IMAGE_NAME}:${BUILD_NUMBER}"
          def DOCKER_IMAGE_LATEST = "${IMAGE_NAME}:latest"
          
          echo "Building Docker image: ${DOCKER_IMAGE_TAGGED}"

          withDockerRegistry(credentialsId: '4235f573-20b7-4053-9d45-c0f8f0e669ba', url: '') {
            
            sh "docker build -t ${DOCKER_IMAGE_TAGGED} -t ${DOCKER_IMAGE_LATEST} ." 
            
            sh "docker push ${DOCKER_IMAGE_TAGGED}"
            sh "docker push ${DOCKER_IMAGE_LATEST}"
            
            echo "Successfully pushed images to Docker Hub."
          }
        }
      }
    }
  }
}
