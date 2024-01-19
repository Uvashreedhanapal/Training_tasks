pipeline {
    agent any

    // parameters {
    //     string(name: 'INPUT_FROM_PIPELINE1', defaultValue: '', description: 'Input from Pipeline1')
    // }

    stages {
        stage('Task3') {
            steps {
                script {
                    echo "Input from Pipeline1: ${params.INPUT_FROM_PIPELINE1}"
                    echo "Hello ${params.INPUT_FROM_PIPELINE1}!...have a nice day!"
                }
            }
        }
    }
    
    post {
        success {
            echo "Pipeline2 completed successfully"
        }
    }
}