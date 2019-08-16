pipeline {
    agent any
    stages {
        stage('Git Clone From Remote Repository') {
            steps {
                sh 'git pull origin master'
            }
        }
        stage('Compose From Docker File'){
            steps{
                sh 'docker-compose up --detach'
            }
          }
        stage('Print Url Body Text With Python'){
            steps{
              sh 'python3.7 WebBodyPrint.py'
            }
          }
        }
}
