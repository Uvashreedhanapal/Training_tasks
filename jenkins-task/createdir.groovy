pipeline {
    agent any

    stages {
        stage('Create Directory') {
            steps {
                script {
                    dir('my_directory') {
                        echo 'Directory created'
                    }
                }
            }
        }

        stage('Create Text File') {
            steps {
                script {
                  
                    writeFile file: 'my_directory/my_file.txt', text: ''
                    echo 'Text file created'
                }
            }
        }
          stage('Write Content to File') {
    steps {
        script {
            def content = 'Hello!....task 5 completed successfully!'
            writeFile file: 'my_directory/my_file.txt', text: content
            echo 'Content written to file'
        }
    }
}

        stage('Print File Content') {
            steps {
                script {
                
                    def fileContent = readFile 'my_directory/my_file.txt'
                    echo "File Content: ${fileContent}"
                }
            }
        }
    }
}