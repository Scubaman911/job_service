"""Main module."""

from flask import Flask
from .cli import job_cli
from .config import Config
from .extensions import scheduler

def create_app():
    app = Flask("jobby")
    app.config.from_object(Config())
    app.cli.add_command(job_cli)

    scheduler.init_app(app)
    scheduler.start()

    return app
    
