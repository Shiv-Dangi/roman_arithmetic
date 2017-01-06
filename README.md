# roman_arithmetic

##This project is a working example of mathematical operation with roman numerals in python.Follow below instruction for the setup of the Project:

Update:

    sudo apt-get update

### Setup Virtual Environment

Create virtual environment and activate it(For virtualenvwrapper you can use http://docs.python-guide.org/en/latest/dev/virtualenvs/)

    sudo pip install virtualenv
    sudo pip install virtualenvwrapper
    sudo sh -c 'echo "export WORKON_HOME=~/Envs" >> ~/.bashrc'
    sudo sh -c 'echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python" >> ~/.bashrc'
    sudo sh -c 'echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc'
    mkvirtualenv venv
    
Clone github repo in your pc
  
    git clone https://github.com/Shiv-Dangi/roman_arithmetic

Activate your virtualenv and Find requirements.txt file in cloned project and run

    pip install -r requirements.txt
    
Run the development server:    

    python manage.py runserver
    
