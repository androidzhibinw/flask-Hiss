## Prepare 
### use virtualenv 
#### why use virtualenv ? 
virtualenv is used to resolve  multiple Python projects using different versions of python or python libraries.
virtualenv can create isolated Python environments as you wish.
learn more about it from [virtualenv](https://virtualenv.readthedocs.org)

#### install virtualenv 

    sudo pip install virtualenv
    mkdir myproject
    cd myproject
    virtualenv venv (name venv whatever you like)
    source venv/bin/activate  (active venv)
    deactivate (deactive venv)

refer [flask-virtualenv](http://flask.pocoo.org/docs/0.10/installation/#virtualenv)
    
###
