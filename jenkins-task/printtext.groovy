pipeline{
    agent any
    stages{
        stage("hello !"){
            steps{
                echo "hello have a great day!!"
            }
        }
    }
}