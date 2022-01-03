# Phoenix-Capstone

# Create Virtual Environment

    python3 -m venv ~/.capstone

# Activate Virtual Environment and Install dependencies

    source ~/.capstone/bin/activate

    pip install flask gunicorn

# Create Flask Application

    from flask import Flask

    def create_app(name: str = 'Hanish Arora'):
    app = Flask(**name**)

        @app.route("/")
        def index():
            return f"Hello World, This is sample application deployed by {name} for Udacity DevOps Capstone! Happy Coding!"

        return app

# Run Application

    # Development Environment

        export FLASK_APP="app:create_app"

        flask run --reload              # With reloading capability without having to re-run app each time after deploying new changes!!!

    # Production Environment

        gunicorn -w 1 --reload -b localhost:5000 "app:create_app(name='Hanish Arora')"

# Add Dependencies

    Add flask/gunicorn dependencies in requirements.txt

    # cat requirements.txt should look like below

        flask
        gunicorn

# Create Dockerfile

    FROM python:3.7.3-stretch

    # Working Directory
    WORKDIR /app

    # Copy source code to working directory
    COPY . app.py /app/

    # Install packages from requirements.txt
    RUN pip install --no-cache-dir 'pip<12' &&\
        pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

    # Expose port 80
    EXPOSE 80

    # Run gunicorn at container launch
    CMD ["gunicorn", "-b", "0.0.0.0:80", "app:create_app(name='Hanish Arora')"]

# Build Docker Image

    docker build --tag=app .

# Run Container locally in bash

    docker run -it app bash

    nohup flask run &

    curl http://127.0.0.1:5000/ to ensure application is responding.

    Outout should look like below:
        root@ebdb876e883b:/app# curl http://127.0.0.1:5000/
        Hello World, This is sample application deployed by Hanish Arora for Udacity DevOps Capstone! Happy Coding!root@ebdb876e883b:/app#

# Run Container Locally

    bash-3.2$ nohup docker run -p 8000:80 app &

    bash-3.2$ curl http://localhost:8000/
    Hello World, This is sample application deployed by Hanish Arora for Udacity DevOps Capstone! Happy Coding!

# Check if Container is running

    bash-3.2$ docker ps
    CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
    f42aaf461af6   app       "gunicorn -b 0.0.0.0…"   43 seconds ago   Up 42 seconds   0.0.0.0:8000->80/tcp   upbeat_burnell

# Stop Container

    docker stop f42aaf461af6
