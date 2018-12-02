# sfproject

clone this repo

    $ git clone https://github.com/noamby/sfproject.git
    
enter the project's folder sfproject

    $ cd sfproject
    
start virtual env with python 3.6

    $ virtualenv -p python3.6 .venv
    
activate the virtual env

    $ source .venv/bin/activate

install requirements

    $ pip install -r requirements.txt
    
enter the project folder sfconreset

    $ cd sfconreset
    
start celery until you see the error

    $ celery -A sfconreset worker -l info -B