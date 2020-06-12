# ExecutiveTable
## This Readme will guide you on how to get your Django server up and running to make changes/modify the backend REST API

First, you want to cd into the directory your local files are and perform a 'git pull' to make sure you have the relevant changes from the master branch.

Next, you want to create a virtual environment in the current directory. Virtual environments are used to create an isolated environment for our server to run. 
  
  
  ### The following commands are used to create a virtual enviroment and start the backend server: 

  After cloning, `cd` into your project directory and run these commands

  * `pip install virtualenv` - ONLY, if you have not installed virtualenv on your machine already

  * `virtualenv venv -p python3` - Creates a virtual environment named venv

  * `source venv/bin/activate` - Activates the virtual environment, 

  Your directory should appear like this: '(venv) user-MBP:ExecutiveTable username$'

  * `pip install -r requirements.txt` - Installs project dependencies inside the virtual environment

  * `pip freeze` - Verify that the installed dependencies match what is inside the requirements.txt file

  * `cd executivetable_restserver`

  Be sure to create a PostgreSQL database named 'executivetable' and a user if needed. 

  * `python3 manage.py migrate` - Run migrations

  * `python3 manage.py runserver` - Opens the development server at localhost:8000

Use `deactivate` to exit the virtual environment. 

  ### The following commands are used to start the frontend server:

  From the root, cd into executivetable_restserver/frontend/executivetable-frontend and run the commands

  * `npm install` - Installs project dependencies inside the directory

  * `npm start` - Opens the development server at localhost:3000

## You have now successfully started up your virtual environment and now it's time to look at our file structure

