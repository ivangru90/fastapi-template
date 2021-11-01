# Documentation for application REST API installation

Here are requirements and installation steps for application API.


## Project structure

Project has four parts:
* app - source code
* Makefile - file where we have defined all tasks which we can run for this project
* Dockerfile - file to build docker application image
* docker-compose.yml - definition of docker-compose, define all needed docker images
* README.md - documentation about project
* requirements.txt - this file contains all necessary python dependencies

### Requirements

You should have installed **Docker** on your machine. It can be downloaded from here https://www.docker.com/products/docker-desktop. 

Everything else will be installed and builded automatically inside docker image.

### Source code structure

Source coude is organized in next way:
* app/
    * api - here are defined endpoints
    * db - here is database initialization and sql scripts
    * model - here are defined database models
    * schema - here are defined DTO objects
    * main.py - here is application defined
    * settings.py - here are defined config variables
* test/

## Steps to install and run application

1. Install Docker on your machine
2. Clone application from repository
3. Open terminal and go to application folder
4. Run start_app.bat -n 

## Development



## How to use application

When all is up, you can go to your web browser and open link **http://localhost:5000/docs**.