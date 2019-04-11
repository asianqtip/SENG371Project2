# SENG 371 Project 2
**_Minimum Effort_**

This is the codebase of the SENG 371 Project 2 prototype as developed by Quynh, Max, and Jared.  
</br>
The purpose of this prototype is to address some of the key concerns that a hypothetical Earth Data Store Observation Platform would face
and give a conceptualization of what might be needed for a future product.  
</br>
Please visit: https://docs.google.com/document/d/17Rm4rD2s79t00I6hPxBv1mBdbo1hP-eilVXdIaQSyRc/edit?usp=sharing
</br>
## Development
### Virtual Environment
Python3.6 is needed for this application. The virtual environment can be setup with 
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
</br>
## Running the tests
Need to create tests
</br>
## Docker setup
### Installation
Docker CE and docker-compose is needed to build the container.
To install docker on your device, visit: https://docs.docker.com/install/
To install docker-compose, run the following command:
```
sudo apt-get install docker-compose
```
</br>
### Building
For Docker:
```
sudo docker build -t app .
sudo docker run app
```
</br>
For docker-compose:
```
sudo docker-compose up
```
</br>


