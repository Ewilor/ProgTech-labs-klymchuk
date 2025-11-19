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
          image 'python:3.12-alpine'
          args '-u=\"root\"'
        }
      }
      steps {
        sh "cp -r $WORKSPACE/* ."
        sh 'mkdir -p test-reports'
        sh 'pip install xmlrunner'
        sh 'python3 tests.py'
      }
      post {
        always {
          junit '**/*.xml'
        }
        success {
          echo 'Tests passed!'
        }
        failure {
          echo 'Tests failed!'
        }
      }
    }
  }
}