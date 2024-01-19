pipeline {
    agent any

    triggers {
        cron('H * * * *')
    }

    stages {
        stage('every one hour') {
            steps {
                script{
                    echo 'Running job every one hour'
                }
            }
        }
    }
}
