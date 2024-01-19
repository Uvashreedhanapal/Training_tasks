
pipeline {
    agent any

    stages {
        stage('task1') {
            steps {
                echo "hii I am ${Name} & my age is ${Age}"
            
               
            }
        }
    }
}