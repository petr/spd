#README 



## Api part

###/tasks

Put the image on server

curl -F "image=@fixtures/members-301f4eab458270d4ad75856b9c7962de.jpg" http://127.0.0.1:8000/api/tasks/


###/tasks/<id>/
curl http://127.0.0.1:8000/api/tasks/1234/

Get the information of task by its id


For development:
styles - only Twitter Bootstrap;
Backbone + lmd - current technologies.
React + webpack - new technologies.



## Setup

### Setup the environment
mkvirtual env spd
pip install -r conf/packages.txt
cd src
./manage.py migrate

### Setup Backbone + lmd
cd assetscore/old
./install.sh

### Setup React + webpack + whatever

TODO

### Runing server
cd src
./manage.py runserver

