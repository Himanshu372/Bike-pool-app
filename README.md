# Bike_pool_app
The repo contains code for bike pooling service. The application is based on Django Rest Framwork. UI is based on HTML, CSS and Vanilla JS.

## Steps to run the code 
### 1
Clone the repo using the command<br>
`git clone https://github.com/Himanshu372/Bike_pool_app.git`<br>
on your local system<br>

### 2 
App has been containerized so that it can run on any system. To able to run the app, please check that Docker is installed on your system(or can be downloaded from here https://www.docker.com/products/docker-desktop)<br>
To create a container run the following command<br>
`docker build -t bike_pool_app .`(A tag of 'bike_pool_app' has been applied to the container)<br>
To run the application, use the following command<br> 
`docker run -it -p 8020:8020 bike_pool_app`<br>
The application is now running on the port 8020, play on!!!!

### 3 
Executing tests<br>
For executing tests, use the following command at the 'tests' directory level inside the app<br>
`./manage.py test bike_app.tests.{test_filename}`<br>


