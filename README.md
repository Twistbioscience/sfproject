# sfproject

1. clone this repo
    ```
    git clone https://github.com/noamby/sfproject.git
    ```

2. enter the project's folder sfproject
    ```
    cd sfproject
    ```

3. start virtual env with python 3.6
    ```
    virtualenv -p python3.6 .venv
    ```
    
4. activate the virtual env
    ```
    source .venv/bin/activate
    ```

5. install requirements
    ```
    pip install -r requirements.txt
    ```
    
6. enter the project folder sfconreset
    ```
    cd sfconreset
    ```
    
7. copy env.sh to your terminal window with parameters
    
8. start celery until you see the error
    ```
    celery -A sfconreset worker -l error -B -c20
    ```