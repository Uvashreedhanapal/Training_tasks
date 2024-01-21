A Docker image is a file used to execute code in a Docker container. Docker images act as a set of instructions to build a Docker container, like a template. Docker images also act as the starting point when using Docker. 

A container is an isolated environment for your code. This means that a container has no knowledge of your operating system, or your files. It runs on the environment provided to you by Docker Desktop.

basic commands:
docker pull: Downloads an image from a registry. (ex: redis)
docker images: List of images in a container
docker ps: List running containers
docker build: Creates a Docker image from a Dockerfile.
docker run: Starts a container from an image.
docker stop: Halts a running container.
docker start: Restarts a stopped container.


Docker Hub-registry service on the cloud that allows you to download Docker images
Docker image -contains application code, libraries, tools, dependencies and other files needed to make an application run
Docker container-instances of Docker images that can be run using the Docker run command
