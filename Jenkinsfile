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
            }
        }
        stage('Deploy Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
                sh 'minikube image load webapp:latest'
                sh 'kubectl rollout restart deployment webapp'
            }
        }
    }
}
