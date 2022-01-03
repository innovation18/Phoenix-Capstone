from flask import Flask


def create_app(name: str = 'Hanish Arora'):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return f"Hello World, This is sample application deployed by {name} for Udacity DevOps Capstone! Happy Coding!"

    return app
