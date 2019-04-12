# SENG 371 Project 2
**_Minimum Effort_**

This is the codebase of the SENG 371 Project 2 prototype as developed by Quynh, Max, and Jared.  
</br>
The purpose of this prototype is to address some of the key concerns that a hypothetical Earth Data Store Observation Platform would face
and give a conceptualization of what might be needed for a future product.  
</br>
Please visit: https://docs.google.com/document/d/17Rm4rD2s79t00I6hPxBv1mBdbo1hP-eilVXdIaQSyRc/edit?usp=sharing

## Development
### Virtual Environment
Python3.6 is needed for this application. The virtual environment can be setup with 
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Running the tests
Currently using Travis CI to automatically run tests every commit. To set this up, simply add text below to the .travis.yml file.
```
script:
  - pytest
```
Files must be properly named using the pytest convention, which is: test_*namehere*.py

## Docker setup
### Installation
Docker CE and docker-compose is needed to build the container.
To install docker on your device, visit: https://docs.docker.com/install/
To install docker-compose, run the following command:
```
sudo apt-get install docker-compose
```

### Building and Running
For Docker:
```
sudo docker build -t app .
sudo docker run app
```

For docker-compose:
```
sudo docker-compose up
```

## Heroku Deployment
The cloud deployment of our app can be found [here](https://dashboard.heroku.com/apps/mineffort/deploy/github).  
If you would prefer to look at our most recent build, click [here](http://mineffort.herokuapp.com/account).  
*Note that the app will require registration with email and password. This email does not have to be a real account*

## Walkthough
If you need any assistance with using the application, or would like a video walkthrough of the application, we have created a two-part guide to our system.</br>
[Part 1](https://drive.google.com/open?id=1QVLl8FdpIeJubv9ryo2QPtxhomGb-kgR) </br>
[Part 2](https://drive.google.com/open?id=1Rqpl6rFAtXzcE2dKf_Lr725yXKtD97mg)
