# codesharing

## Roadmap / Todo

- Make a markdown editor 
- Create a login and signup system.
- Server Sync of user data, markdown etc.
- Feature to add code snippit in markdown.
- Execution of code and show live output.
- Add your own feature.

##### Repository Name suggestion:

- Stupid_Markdown
- Something-Cool

> ###### Add your own ideas/features, name suggestion for repository, extra edit
--- 

### Setup Database on Docker

```sh
sudo pacman -S docker # install docker
sudo systemctl start docker # starts docker service
# whenever computer starts use above command to start docker.service 
```
```sh
docker pull postgres:alpine # download small(alpine) image of postgres
# creating container named 'postgres-0' with POSTGRES_PASSWORD with image 'postgres:alpine'.
sudo docker run --name postgres-0 -e POSTGRES_PASSWORD=rajat -d -p 5432:5432 postgres:alpine 
sudo docker start postgres-0 # start container named 'postgres-0'
```

```sh
sudo docker exec -it postgres-0 bash # open bash inside your terminal connecting to docker running container named 'postgres-0'
psql -U postgres # open psql command line for psql / sql commands.
# exit out of it.
```
```sh
# open postgres commandline of your docker container from your terminal.
psql -h localhost -p 5432 -U postgres
create database test; # sql command to create database named 'test'
```
## Commands for pSQL (postgresql)
```bash
\c test #connect to database named 'test'
\l # list all database
\d # see all the relation in database.
\du # list all users and their roles.
```
##### all sql command words as usually inside pSQL commandline.

## Add database to Django.
In settings.py 
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
        'PASSWORD' : 'rajat'
    }
}

```

## Docker Commands Commonly used
```bash
docker container ls [OPTIONS]
docker container ls -a  # list all running container [id, image in use ,status, etc.]

docker stop [CONTAINER_NAME]  # stops a container.
docker start [CONTAINER_NAME] # starts a container

docker container rm [CONTAINER_NAME] # deletes a container by name.
docker container rm ccc3f2ff1cab c3f2ff1cab  # delete two container by 'id'

docker rm $(docker ps -aq) # to clean all container
docker rm -f $(docker ps -a -q) # to stop all docker container
```
## Github Help

- To check all the commits till date on all the branches. or [Direct Link](https://github.com/rajat98v/codesharing/network)
    - Go to Insights Tab on Github Repo.
    - Go to Network on Left menu.
    - Click on small Dots on any brach or contributor to see commit comment.
