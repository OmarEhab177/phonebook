# Running the `PhoneBook` Project in a Docker Container
#### This project can be run in a Docker container, allowing you to easily set up and manage dependencies. The following instructions will guide you through the process of setting up and running the project using Docker.

## Prerequisites
- Docker must be installed on your machine.
- This project should be cloned or download in your local machine.

#### clone the project to your machine

```
git clone https://github.com/OmarEhab177/phonebook.git
```

## Building the Image
1. Open a terminal and navigate to the root directory of the project.
2. Build the Docker image by running the command:

```
docker build -t phonebook .
```

#### This command will build an image with the name `PhoneBook` using the `Dockerfile` present in the project root directory.

## Running the Container
1. Start a new container using the image you just built by running the command:

```
docker run -p 8000:8000 phonebook
```
#### This command will start a new container based on the `phonebook` image and map port 8000 in the container to port 8000 on your local machine.

2. Open a web browser and navigate to `http://localhost:8000` to access the project.

### With these commands, you should be able to run the Django project in a Docker container, making it easy to set up and manage dependencies.