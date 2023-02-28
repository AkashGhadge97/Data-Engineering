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
