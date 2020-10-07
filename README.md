# codesharing

## Done
- Registration and Login using Postgres sql

## Roadmap / Todo

- Migrate project to virtualenv
- Make a markdown editor 
- Create a login and signup system.
- Server Sync of user data, markdown etc.
- Feature to add code snippit in markdown.
- Execution of code and show live output.
- ADD YOUR OWN FEATURE.

##### Repository Name suggestion:

- Stupid_Markdown :)
- Something-Cool

> ###### Add your own ideas/features, name suggestion for repository, extra edit
--- 

### Setup Database on Docker

```bash
sudo pacman -S docker # install docker
sudo pacman -S postgresql python-django python-django-allauth # install postgresql
yay -S python-social-auth-app-django
sudo systemctl start docker # starts docker service
# whenever computer starts use above command to start docker.service 
```
```bash
sudo docker pull postgres:alpine # download small(alpine) image of postgres
# creating container named 'postgres-0' with POSTGRES_PASSWORD with image 'postgres:alpine'.
sudo docker run --name postgres-0 -e POSTGRES_PASSWORD=rajat -d -p 5432:5432 postgres:alpine 
sudo docker start postgres-0 # start container named 'postgres-0'
```

```bash
sudo docker exec -it postgres-0 bash # open bash inside your terminal connecting to docker running container named 'postgres-0'
psql -U postgres # open psql command line for psql / sql commands.
# exit out of it.
```
```bash
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
#### [Video on SQL](https://www.youtube.com/watch?v=HXV3zeQKqGY&t=11291s)

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


##### Important commands

```bash
git checkout BranchName # to change working branch locally.
git branch FrontEnd # create branch named 'FrontEnd'
# A local branch will not delete if the branch is active so change to another branch.
git branch -d FrontEnd # delete local branch 'FrontEnd' 
git branch -D FrontEnd # force delete local branch 'FrontEnd' irrespective of its merge status.
```

[Video on Git Collaboration](https://www.youtube.com/watch?v=MnUd31TvBoU)  
Notes on above video

#### Create New BRANCH for adding new major feature.

```bash
git checkout master # to check if your master branch is updated.
git pull origin master # to pull all the updates.
git checkout -b FrontEnd # to create new branch named 'FrontEnd'
# make changes
git add . # add all the new files.
git commit -m "add react support" # make a commit locally.
git push origin FrontEnd # to push to 'FrontEnd' branch on server.
```


#### Edit a feature/BRANCH


```bash
git pull origin manager # to renew your copy of repository from master branch.
# commit your changes to your local repository or origin master before above command.
# It you want to work on 'FrontEnd' branch
git checkout -b FrontEnd # activate branch 'FrontEnd'
# all file on your system will be automatically changed to that branch
# Edit the branch 
git add . # add all the changes
git commit -m "My front end changes" # commit to your local FrontEnd branch.
git push FrontEnd # push changes to 'FrontEnd' branch on server.
# click "Compare & pull request" on 'Front End' branch to make a request to merge with master branch.
# write about your pull request and click "Create Pull Request". It will be then reviewed and added to master.
# if you want to autheticate pull request on your own just click "Merge pull request" yourself since you are a collaborator on project and you have admin writes to merge branchs.
```

- To check all the commits till date on all the branches. 
    - Go to Insights Tab on Github Repo.
    - Go to Network on Left menu.
    - Click on small Dots on any brach or contributor to see commit comment.
    - [Direct Link to do above](https://github.com/rajat98v/codesharing/network)
- To use the Auth feature of facebook, Install following packages:
    ```bash
    pip install django-allauth
    pip install social-auth-app-django
    ```
