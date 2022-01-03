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
