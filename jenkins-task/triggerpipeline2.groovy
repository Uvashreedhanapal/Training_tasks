pipeline {
    agent any

    stages {
        stage('Initialize') {
            steps {
                echo 'Initializing Pipeline 2...'
            }
        }

        stage('task...') {
            steps {
                script {
                    def number = 3
                    def cube = number * number * number
                    echo "cube: ${cube}"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline 2 completed.'
        }
    }
}
