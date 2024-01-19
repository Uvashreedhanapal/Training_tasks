pipeline {
    agent any
    
    environment {
        VALUE_TO_PASS = 'uva'
    }

    stages {
        stage('Task1') {
            steps {
                script {
                    echo "Value to pass to Pipeline2: ${VALUE_TO_PASS}"
                    echo "Setting env variable for Pipeline2"
                    env.VALUE_FROM_PIPELINE1 = VALUE_TO_PASS
                }
            }
        }
    }
    
    post {
        success {
            echo "Pipeline1 completed successfully"
            build job: 'job7.2', parameters: [string(name: 'INPUT_FROM_PIPELINE1', value: env.VALUE_FROM_PIPELINE1)]
        }
    }
}
