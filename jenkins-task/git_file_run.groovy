pipeline {
    agent any

    stages {
        stage('Checkout Repository') {
            steps {
                script {
                    git branch: "new_branch", url: 'https://github.com/Uvashreedhanapal/Training_tasks.git'
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    
                    dir("C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\job10\\jenkins-task") {
                        bat 'sample.py'
                    }
                }
            }
        }
    }
}
