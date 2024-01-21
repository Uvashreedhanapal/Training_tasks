JENKINS:
------------
1)What is jenkins..?
Jenkins is an automation tool that is open-sourced and written in Java and has plugins built for continuous integration. Jenkins is used to building software projects and test them continuously, allowing developers to integrate any changes in their projects easily.

2)What are all the operations we can do in jenkins.
Jenkins supports various operations, including job creation, scheduling, building, testing, and deploying software. It provides a centralized automation server for continuous integration and delivery, streamlining the software development lifecycle.

3)What is CI/CD..?
CI/CD stands for Continuous Integration and Continuous Delivery. It is a software development practice that involves automatically testing and integrating code changes frequently (CI) and delivering these changes to production in a consistent and automated manner (CD), enabling faster and more reliable software releases.

4)Explore what programming languages Jenkins will support to create a pipeline?
Jenkins supports a wide range of programming languages for creating pipelines, including but not limited to Java, Groovy, Python, Ruby, and Shell scripting.

5)What is groovy script?
A Groovy script is a dynamic scripting language that runs on the Java Virtual Machine (JVM). In the context of Jenkins pipelines, Groovy is commonly used to define the workflow and automation logic.

6)groovy syntax and basic concepts? 
  Variables: Declare using def keyword (e.g., def myVariable = 10).
  Print Statements: Output with println("Hello, World!").
  Strings: Define with single or double quotes (e.g., "Hello" or 'World').
  Lists and Maps: Create lists [1, 2, 3] or maps ['key': 'value'].
  Conditionals: Use if-else statements for decision-making.
  Loops: Employ for and while loops for iteration.
  Methods/Functions: Define reusable code blocks.
  Pipeline Steps: Special syntax for Jenkins pipelines.
    pipeline {
        agent any
        stages {
            stage('Build') {
                steps {
                    // build steps
                }
            }
            stage('Deploy') {
                steps {
                    // deployment steps
                }
            }
        }
    }          
      “Pipeline” defines the block that will contain all the script content.
      “Agent” defines where the pipeline will be run, similar to the “node” for the scripted one.
      “Stages” contains all of the stages.


7)Explore steps, stage, dir, script, post, git, when, expression, if concepts?

  steps: The steps block contains a series of individual build steps. Each step represents a task or command to be executed in the build process.  
  stage: The stage block is used to define a logical division in the pipeline. It helps organize and visualize the progression of the build process. Stages often represent phases like "Build," "Test," or "Deploy." 
  dir: The dir step changes the current working directory for the enclosed block of steps. This is useful when you need to execute commands in a specific directory.
  script: The script block allows the execution of arbitrary Groovy code. It is often used for more complex logic that goes beyond the capabilities of individual build steps.
  post: The post block defines actions to be taken after the completion of the pipeline or a specific stage. Commonly used for cleanup tasks or notifications.
  git: The git step configures Git settings for the pipeline, such as specifying the repository URL, credentials, and branch.
  when: The when directive specifies conditions under which a stage or a step should be executed. It allows for conditional execution based on various factors like branch, environment variables, or expression evaluation.
  expression: In the context of when, an expression is a condition that evaluates to true or false. It can involve comparing strings, numbers, or checking the state of certain variables.
  if: The if statement is often used within a script block to conditionally execute certain code based on a specific condition. It provides more granular control over the flow of execution within the Groovy script.

8)Explore available parameter types which we can pass to the pipeline.
  String Parameter:
    Defined using the string parameter type.
    Accepts a free-form text input.
  
        parameters {
            string(name: 'ENVIRONMENT', defaultValue: 'dev', description: 'Target environment')
        }
        
  Choice Parameter:
      Defined using the choice parameter type.
      Provides a dropdown list of predefined choices.
  
        parameters {
            choice(name: 'BRANCH', choices: ['master', 'develop'], description: 'Select branch')
        }
        
  Boolean Parameter:
    Defined using the booleanParam parameter type.
    Represents a true/false or on/off option.
    
        parameters {
            booleanParam(name: 'CLEAN_BUILD', defaultValue: true, description: 'Perform a clean build')
        }
        
  Password Parameter:
    Defined using the password parameter type.
    Masks the input to keep it confidential.
  
        parameters {
            password(name: 'API_KEY', defaultValue: '', description: 'Enter API key')
        }
        
  File Parameter:
    Defined using the file parameter type.
    Allows users to upload a file as a parameter.
  
        parameters {
            file(name: 'UPLOAD_FILE', description: 'Select file to upload')
        }
        
  Text Parameter:
    Defined using the text parameter type.
    Accepts multi-line text input.
  
        parameters {
            text(name: 'RELEASE_NOTES', defaultValue: '', description: 'Enter release notes')
        }

9)What is periodic build in jenkins?        
In Jenkins, a periodic build is a scheduled automatic execution of a job at specified time intervals. It allows users to regularly run tasks, such as testing or deployment, without manual initiation.



