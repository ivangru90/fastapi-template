@echo off

set var=%1

if "%var%"=="" GOTO empty 

if %var%==-s (
    echo "Stop application"
    call docker-compose --project-name app down
    GOTO end 
)

if %var%==-r (
    echo "Stop application, remove all volumes and only application image"
    call docker-compose --project-name app down
    call docker volume rm -f app_dbdata
    call docker volume rm -f app_pgadmindata
    call docker volume rm -f app_liquibasedata
    call docker image rm -f app_springapp
    GOTO end 
)

if %var%==-a (
    echo "Stop application, remove all volumes and all images"
    call docker-compose --project-name app down
    call docker volume rm -f app_dbdata
    call docker volume rm -f app_pgadmindata
    call docker volume rm -f app_liquibasedata
    call docker volume prune
    call docker image rm -f app_app
    call docker image rm -f liquibase/liquibase
    call docker image rm -f dpage/pgadmin4
    call docker image rm -f postgres
    call docker image prune
    GOTO end 
)

:empty
echo "Please set parameter: -s to stop application, and -r to stop application and remove existing volumes"

:end