# SETUP
## Before install
You may need to install Python 3.9 and virtualenv. If you have them already, you can skip next steps.
- Install python3.9. This project may not work with other versions.
```console
$ sudo apt-get install python3.9
```
- Install virtualenv. We will need it to isolate our libraries and project.
```console
$ sudo pip install virtualenv 
```
## Install
- Clone this repository:
```console
$ git clone https://git@github.com:yuwinzer/x_project.git
$ cd vehicles_and_drivers
```
or you can download project ZIP, extract it and enter the folder:
```console
$ cd vehicles_and_drivers
```
- Create virtual environment with virtualenv:
```console
$ virtualenv env virtualenv --python=/usr/bin/python3.9
```
- Activate virtual environment:
```console
$  source venv/bin/activate
```
- Install the required libraries:
```console
$ pip install -r requirements.txt
```
- Make migrations:
```console
$ python manage.py makemigrations
$ python manage.py migrate
```
## Run 
To run project you need execute the following command: 
```console
$ python manage.py runserver
```
Then follow the link:: http://127.0.0.1:8000/api/