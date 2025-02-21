# StrongMind Pizza Management Application

## Overview
This project is brought to you by Hunter Jones as part of a StrongMind Full Stack Developer application. This simulated task showcases self-organized work to measure working within the team as part of the technical interview process. The exercise involves creating an application which can create and manage Pizzas. This application will be deployed to a cloud provider for access.

## Thought Process
Thought process behind technical choices **Pending**
- I decided to use Flask for its lightweight framework with the option to add functionality as I develop.
- Postgres is the database of choice for its more advanced features, concurrent superiority operations, and scalability.
- Authentication is implied with multiple roles specified under user stories and routes are restricted to limit login required for access to functions connecting to the database.
- Cloud Run is a cost effective way to scale a small applicaiton with start from zero minimum instance policies enabled.
- Docker containerization allows development into an image that can be started in multiple enviroments and cloud providers.

## Features
Notable features encompassing the project.

### Manage Toppings
As a pizza store owner you are able to manage toppings available for your pizza chefs.
- It shows you a list of available toppings.
- It allows you to add a new topping.
- It allows you to update or delete an existing topping.
- It ensures you do not enter duplicate toppings.

### Manage Pizzas
As a pizza chef you should be able to create new pizza master pieces.
- It allows you to see a list of existing pizzas and their toppings.
- It allows you to create a new pizza and add toppings to it.
- It allows you to delete or update an existing pizza.
- It allows you to update toppings on an existing pizza.
- It ensures you do not enter duplicate pizzas.

### Data Persistance
- Data persistance is handled with a dedicated Google Cloud SQL Postgres instance

### User Interface
- Responsive Design aspects using viewport and flexbox

### Deployment
- App Deployment method: Google Cloud Run
- Database Deployment method: Google Cloud SQL

## How to use
Instructions on how to use the application as an end user.

### As an Owner
1. Login with credentials
2. Username: 'pizzamindowner'   Password: 'password1'
3. Click Manage Toppings link available in navigation bar
4. Insert a new topping name and click Create Topping button to add a new topping
5. From Current Toppings section click Delete button to remove a topping form the available options
6. Click Logout from navigation bar to remove current session credentials

### As a Chef
1. Login with credentials
2. Username: 'pizzamindchef'    Password: 'password2'
3. Click Manage Pizzas link available in navigation bar
4. Insert a new pizza name and click Create Pizza button to add a new pizza
5. Select Delete button to remove the pizza
6. Select Manage button to navigate to the individual pizza page
7. Under Available Toppings section select the Add button next to a topping you would like to add
8. Under Current Toppings section select the Remove button next to a topping you would like to remove
9. Click logout from navigation bar to remove current session credentials

## Technologies
This is a list of technologies used across the entire application.

1. **Languages/Framework**
  - Python
  - JavaScript
  - HTML
  - CSS
  - Flask

2. **Database**
  - SQL: Postgres
  - Connector: psycopg2

3. **Tools/Services**
  - GitHub
  - Docker Desktop
  - Docker
  - Visual Studio Code
  - Google Cloud Platform
  - Google Cloud Run
  - Google Cloud SQL
  - Postgres
  - Postbird

## Instructions
Detailed instructions on how to build and run locally.

### Before You Get Started
- pizza-app is the top level directory for running the containerized application
- Other directories at this level are for configuration and independent projects

### Build and Run Locally
Instructions on how to build locally:
#### Download Software
1. [Download Docker Desktop](https://www.docker.com/get-started/)
2. [Download Postgres](https://postgresapp.com)
3. [Download Postbird](https://github.com/paxa/postbird)

#### Clone Repository
In your terminal navigate to a directory you would like to use and run
```bash
git clone https://github.com/joneshu2/strongmind.git
```

#### Set Up Local Database
- Make sure your postgres.app is currently running a server
- Navigate to your postbird applicaiton to use as a graphical manager for quick sql setup.
- Select the default option and click connect.
- Select database and choose the option to create a new database named 'strongmind'.
- Within this database select the query tab to paste in the contents of the db_init.sql file.
- Click Run Query to populate tables in the correct order and initial users required for testing.

#### Build Application for Local Testing
- Make sure Docker Desktop is open and initial installation has been followed based on the above guide.
- Navigate to your directory under strongmind so that
```bash
pwd
```
displays
```bash
strongmind/pizza-app
```
with the Dockerfiles and compose.yaml listed inside the directory.
- From here type the command
```bash
docker compose up
```
- This will use the compose file to build the dockerfile marked Dockerfile-dev for local testing.
- Navigate to localhost:8080 in your browser to access the built application.
- To pause the container navigate to the container image in Docker Desktop and click the square pause button.
- Delete the container when done by selecting the square to the right of the container name and click delete.

## Resources
Resoures used in development will be updated and listed below as the application is developed.
- [Docker](https://www.docker.com)
- [Flask](https://flask.palletsprojects.com)
- [Visual Studio Code](https://code.visualstudio.com)
- [Python Documentation](https://docs.python.org)

## Contributers
The Project idea was created by [StrongMind](https://www.strongmind.com) and implemented by [Hunter Jones](https://www.linkedin.com/in/hunter-r-jones). Contributer relevant links are also listed below.
- Project Ideation(GitHub): [StrongMind GitHub Assignment](https://github.com/StrongMind/culture/blob/main/recruit/full-stack-developer.md)
- Project Implementation(GitHub): [Hunter Jones](https://github.com/joneshu2)
