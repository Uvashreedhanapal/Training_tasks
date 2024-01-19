pipeline {
    agent any
    
    parameters {
        string(name: 'DYNAMIC_VALUE', defaultValue: 'Default_Value', description: 'Enter a dynamic value')
    }

    stages {
        stage('Print Dynamic Value') {
            steps {
                script {
                    
                    def dynamicValue = params.DYNAMIC_VALUE
                    echo "Dynamic Value is: ${dynamicValue}"
                }
            }
        }
    }
}
