pipeline {
    agent any

    stages {
        stage('Initialize') {
            steps {
                echo 'Initializing Pipeline 1...'
            }
        }

        stage('Task - Square') {
            steps {
                script {
                    def number = 5
                    def square = number * number
                    echo "Ans: ${square}"
                }
            }
        }

        stage('Trigger Pipeline 2') {
            steps {
                echo 'Triggering Pipeline 2...'
                build job: 'job6.2', wait: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline 1 completed.'
        }
    }
}
