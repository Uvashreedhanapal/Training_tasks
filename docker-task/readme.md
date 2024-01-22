A Docker image is a file used to execute code in a Docker container. Docker images act as a set of instructions to build a Docker container, like a template. Docker images also act as the starting point when using Docker. 

A container is an isolated environment for your code. This means that a container has no knowledge of your operating system, or your files. It runs on the environment provided to you by Docker Desktop.

Docker Hub-registry service on the cloud that allows you to download Docker images

Docker image -contains application code, libraries, tools, dependencies and other files needed to make an application run

Docker container-instances of Docker images that can be run using the Docker run command

basic commands:
    docker pull: Downloads an image from a registry. (ex: redis)
    docker images: List of images in a container
    docker ps: List running containers
    docker build: Creates a Docker image from a Dockerfile.
    docker run: Starts a container from an image.
    docker stop: Halts a running container.
    docker start: Restarts a stopped container.


Port forwarding:
    In Docker, port forwarding is typically achieved by mapping ports between the host machine and the container.
    For example, if you have a Flask app running on port 5000 inside the container, and you want to access it on port 8080 on the host, you would run:
            docker run -p 8080:5000 flask_image 

comments:
    to build: docker build -t flask .  
    to run app: docker run -p 5000:5000 flask
    