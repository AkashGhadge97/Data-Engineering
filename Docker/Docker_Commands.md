# Docker Commands

## Manage Docker Images

  _**1. docker pull IMAGE[:TAG]**_  - Download a docker image  e.g _docker pull mysql_

  _**2. docker push IMAGE**_ - Upload an image to a repository e.g _docker push myimage:1.0_

  _**3. docker rmi IMAGE**_ - Delete an image

  _**4.docker images**_ - Show list of all images

  _**5. docker image prune**_ - Delete all dangling images

  _**6. docker image prune -a**_ - Delete all unused images

  _**7. docker build DIRECTORY**_  - Build an image from a Dokerfile

  _**8. docker build -t IMAGE DIRECTORY**_ - Build and tag an image from a Dockerfile e.g d_ocker build -t myimage ._
  
 ## Run a new container
 
_**1. docker run IMAGE**_ - Start a new container from an image  _e.g docker run mysql_

_**2. docker  run --name CONTAINER IMAGE**_ - Start a new container from an image by assigning a name to it. e.g _docker run --name newmysqlcont mysql_

_**3. docker run -p HOSTPORT:CONTAINERPORT IMAGE**_ - Start a new container by mapping it to a new port (Running on ne wport) e.g _docker run  -p 8087:8081 mysql_

_**4. docker run -d IMAGE**_ - Start a container in background e.g _docker run -d mysql_

_**5. docker run --hostname HOSTNAME IMAGE**_ - Start a container by assigbing it a new name e.g _docker run --hostname dbserver mysql_

## Manage Containers

_**1. docker ps**_ - Show a list of running containers

_**2. docker ps -a**_ - Show a list of all containers

_**3. docker rm CONTAINER**_ -  Delete a container

_**4. docker CONTAINER prune**_ - Delete a stopped container

_**5. docker stop CONTAINER**_ - Stop a running container

_**6. docker start CONTAINER**_ - Start a stopped container

_**7. docker exec -t CONTAINER EXECUTABLE**_ - Start a shell inside a running container e.g _docker exec -it web bash_

_**8. docker rename OLD_NAME NEW_NAME**_ - Rename a container e.g _docker rename mysql mysqlnew_

_**9. docker commit CONTAINER**_ - Create an image out of container
