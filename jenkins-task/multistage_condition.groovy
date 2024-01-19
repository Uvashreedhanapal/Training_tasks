pipeline {
    agent any
    
    stages {
        stage('Task1') {
            steps {
                echo "hello ${params.name}"
            }
        }
        
        stage('Task2') {
            when {
                expression { params.saveInfo == 'Yes' }
            }
            steps {
                echo "your info saved successfully!"
            }
        }
        
        stage('Task3') {
            steps {
                echo "Welcome to Jenkins! ${params.name}"
            }
        }
    }
}
