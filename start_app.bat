@echo off

set var=%1

if "%var%"=="" GOTO empty 

if %var%==-n (
    echo "Build fresh application and db, and start it"
	call docker-compose --project-name app build
	call docker-compose --project-name app up
) 

if %var%==-e (
    echo "Start existing application and db"
    call docker-compose --project-name app up
)

if %var%==-b (
    echo "Build application and use existing db, and start it"
    call docker-compose --project-name app build backend
    call docker-compose --project-name app up
)

GOTO end 

:empty
echo "Please set parameter: -n to build application from scratch and start, -e to start application with existing docker images, -b to build application and use existing db image"

:end