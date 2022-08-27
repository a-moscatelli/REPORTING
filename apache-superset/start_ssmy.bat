
@echo docker service is assumed up
@echo any new image will be auto-pulled if needed

rem https://github.com/abhioncbr/docker-superset/blob/master/docker-files/.env

set MYSQL_USER=superset
set MYSQL_PASSWORD=superset
set MYSQL_DATABASE=superset
set MYSQL_ROOT_PASSWORD=root

# redis environment variables.
set REDIS_HOST=redis
set REDIS_PORT=6379

# superset environment variables.
set MYSQL_HOST=mysql
set MYSQL_PORT=3306
set SUPERSET_ENV=local
set SUPERSET_VERSION=2.0.0
set SUPERSET_VERSION=1.5.1
set SUPERSET_VERSION=0.29.0rc5


call docker-compose -f docker-compose-ssmy.yml up -d

@echo wait 2-3 min
@echo enjoy http://localhost:8080/login/
@echo login as "admin/admin"
@echo then you can go to menu "databases" and 
rem https://dzone.com/articles/docker-image-of-apache-superset

