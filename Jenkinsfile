pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Azepuo/devops-lab.git'
            }
        }
        stage('Build & Push Docker') {
            steps {
                sh 'docker build -t yasssine22/webapp:latest .'
                sh 'docker push yasssine22/webapp:latest'
            }
        }
        stage('Deploy Kubernetes') {
            steps {
                echo 'Image built successfully. Deploying to Kubernetes...'
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
                sh 'kubectl rollout restart deployment webapp'
            }
        }
    }
}