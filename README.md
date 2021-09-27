# dining_hall

## NP Laboratory 1

### RUN

$ # clone repository
$ pip install -r imports.txt 
$ py dining_hall.py 

### with docker

$ docker build -t dining . # create kitchen image
$ docker run -d --net pr_lab1 --name dining dining # run docker container on created network
