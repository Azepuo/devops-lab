pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Azepuo/devops-lab.git'
            }
        }
        stage('Build Docker') {
            steps {
                sh 'docker build -t webapp:latest .'
                sh 'minikube image load webapp:latest'
            }
        }
        stage('Deploy Kubernetes') {
            steps {
                echo 'Image built successfully. Deploying to Kubernetes...'
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
                sh 'kubectl rollout restart deployment/webapp'
            }
        }
    }
}