# CS-499-Gymnastics-Scoreboard

## Environment Information
We will be using the following tools:
```
python 3.12.x
mysql 8.3.0
docker
docker compose 3.3
```

In addition, the `requirements.txt` file contains the Python Packages that we are using. The version should be specified for any new package installed.

### Requirements.txt Packages:
- PyQt5 - Our chosen GUI Library
- sqlalchemy - Database Object Relational Mapping (ORM) tool
- python-dotenv - Loads .env files into into the process's environment for DB access
- mysqlclient - The client we use for connecting SQLAlchemy to MySQL


## Environment Setup
Make sure to install the tools listed above (python, docker/docker-compose) before following these steps.
1) Navigate to the correct folder by running `cd ./db_setup/`.
2) Run `docker compose up` This should start the docker container.
3) Once the DB is started, open another terminal.
4) Navigate to the correct folder by running `cd ./testing/`.
5) Run `python db_setup_script.py` and make sure there are no errors.
6) Navigate to the src folder by running `cd ../src/`.
7) Run `python main_controller.py`. If everything worked, the application should run.

## Git Repository Rules
All changes should be merged into the `main` branch using a pull request. One approval is required, ideally from someone other that the person who wrote the code. The review does not need to be super in depth.

This will help us make sure our code is good.

### Branches
- We should try to name our branches based on what we are working on.
    >**For Example:** My first branch name is `bm/repo-setup`. `bm` for Ben Morrison, and `repo-setup` because that's what I was doing.
