# Django-Multimedia-Content-Manager

#### Video Demo:  
<https://www.youtube.com/watch?v=QdZHWHps21g>

#### Description:
A Django web app for manage multimedia content

* Create, edit and delete multiemdia contents
* Create, edit and delete posts
* Create, edit and delete learning paths

#### Environment:
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3) supported by Docker-Compose

#### Installation:
* Clone this repository: `git clone "git@github.com:Jaricapa-holberton/proyecto1.git"`
* Install Docker-Compose: `sudo apt  install docker-compose`
* Use this command on the project's root folder: `export COMPOSE_FILE=local.yml`
* Build image and run image: `sudo docker-compose -f docker-compose.yml up --build`
* Create superuser if don't exists: `docker-compose -f docker-compose.yml run --rm django python manage.py createsuperuser`
* Open the web app in a browser: `http://127.0.0.1:8000/`

#### Examples of use:
interact with the application in the browser as if it were a CMS

#### Bugs:
No known bugs at this time. 

#### Authors:
Jaime Aricapa - [Github](https://github.com/Jaricapa-holberton)

#### License:
Public Domain. No copy write protection. 

