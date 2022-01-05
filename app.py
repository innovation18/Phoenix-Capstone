from flask import Flask


def create_app(name: str = 'Hanish Arora'):
    app = Flask(__name__)

    @app.route("/")
    def dummy():  # https://stackoverflow.com/questions/10107350/how-to-handle-the-pylint-message-idw0612-unused-variable
        return f"Hello World!, This is sample application:v2 from deployed by {name} for Udacity DevOps Capstone! Happy Coding!"

    return app
