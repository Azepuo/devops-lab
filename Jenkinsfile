pipeline {
    agent any
    stages {
        stage('Merge') {
            steps {
                git branch: 'main', url: 'https://github.com/Azepuo/devops-lab.git'
            }
        }
        stage('Build Docker') {
            steps {
                bat 'docker build -t webapp:latest .'
            }
        }
        stage('Deploy Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
}
