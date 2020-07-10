# Deployment

Deployment is designed to work with docker and docker-compose.

### Prerequisites

- [docker][docker]
- [docker-compose][dc]


[docker]: https://www.docker.com/
[dc]: https://docs.docker.com/compose/

### Procedure

- copy the example environment file:
 ```
 cp prod-variables.env.example prod-variables.env
```

- edit the variables file, fill in the appropriate values and uncomment them

- build the app with

```shell script
docker-compose -f docker-compose.yml -f docker-compose-prod.yml --env-file prod-variables.env build
```
- launch the server with

```shell script
docker-compose -f docker-compose.yml -f docker-compose-prod.yml --env-file prod-variables.env up -d
```

- run the migrations

```shell script
docker exec <id of the web container> python3 manage.py migrate
```


# Development setup

### Using docker

- run the runDev script:

```shell script
./runDev.sh
```

Running the script with the `-n` argument will skip the build phase.

Running the script with the `-m` argument will also run the migrations.

Any code changes should update automatically without having to restart the container.

This will start the default django development server on port 8000 
but uses a postgresql container for the database.


### Flask only

- run the following command
```shell script
ENV=dev python manage.py runserver 8000
```

This will start the default django dev server on port 8000 with an sqlite database. 

- run the migrations with
```shell script
python manage.py migrate
```
