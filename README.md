# Deployment


## Docker + postgres + nginx

This is the recommended deploy method, using the provided docker image for the application
in combination with a native installation of postgres and a reverse proxy.

### Prerequisites

- [postgres 11][postgres] (it is recommended to use your distributions package manager to install postgres, 
  look for specific installation guides for your distro)
- [nginx 1.18.0][nginx]
- [docker 20.10.5][docker]
- git

The abovementioned versions are the ones that are actively used and supported,
other versions may work as well but are untested.

### setup

- Setup the database. Default name is `noagreements` but you are free to choose
  a different name, just be sure to configure it correctly (see below)


- create a database user. Again, default is `noagreements`, but a different name can
  be configured. Grant the [required permissions][django-req-perm] to this user and make sure
  to select a strong password.
  
- make sure postgres is setup to receive outside connections. To do so:
  - find postgresql.conf with `find / -name "postgresql.conf"`
  - edit the file and set the `listen_addresses` key to `'*'`
    - edit `pg_hba.conf` which lives in the same directory, and append the following lines:
      (replacing noagreements with the database and user name, respectively, in each line)
    ```
    host    noagreements    noagreements    0.0.0.0/0
    host    noagreements    noagreements    ::/0
    ```
  - restart the postgres server

- Clone this repo. Use the master branch for the production build, and the development 
branch for the staging build. Any commands past this point assume your working dir 
  is the project's root.
  

  
- build the docker image (using tag is optional but recommended:
  `docker build . --tag noagreements:latest`
  
- setup a docker network
  `docker network create -d bridge --subnet 192.168.0.0/24 --gateway 192.168.0.1 noagreements-net`

- configure the required environment variables. See prod-variables.env.example for
  a detailed overview. Either use an env-file or multiple -e directives
  
- start the docker container (use the tag of the image you created earlier):
`docker run \
  -p 8000:80 \
  --env-file prod-variables.env \
  --network noagreements-net \
  --name noagreements-site -d noagreements:latest`
  
- setup an nginx config to route requests to the docker container

[postgres]: https://www.postgresql.org/docs/11/tutorial-install.html
[nginx]: https://nginx.org/en/
[django-req-perm]: https://docs.djangoproject.com/en/3.1/topics/install/#get-your-database-running



# Development setup

### Prerequisites:
- python 3.9.2
- sqlite 3.35.4

(again, later versions are probably fine but untested)


### Procedure

- (optional but recommended) create and activate a python virtual environment
- install prerequisites: `pip install -r requirements.txt`

- run the following command
```shell script
ENV=dev python manage.py runserver 8000
```

This will start the default django dev server on port 8000 with an sqlite database. 

- run the migrations with
```shell script
python manage.py migrate
```
