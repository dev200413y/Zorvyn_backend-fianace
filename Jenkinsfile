pipeline{
    agent any
    stages{
        stage('Clone')
        {
            steps{
                checkout scm
            }
        }
        stage('Build Docker Image')
        {
            steps{
                sh "docker build -t zorvyn-finance-backend ."
                }
            }
        stage('Run Tests'){
            steps{
                sh "docker run --rm zorvyn-finance-backend pytest tests/ -v"
        }
        }
        stage("Deploy"){
            steps{
    
                sh "docker-compose down"
                sh "docker-compose up -d"

            }
    
        }
    }
    post{
        sucess {
            echo 'pipeline completed successfully!'
        }
        failure {
            echo 'pipeline failed !'
        }
    }
}