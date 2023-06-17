"""Console script for jobby."""
import sys
import click
from flask.cli import AppGroup
from . import jobs

job_cli = AppGroup('job')

@job_cli.command("hello_jobby")
@click.command()
def hello_jobby(args=None):
    """Console script for jobby."""
    jobs.hello()


if __name__ == "__main__":
    sys.exit(hello_jobby())  # pragma: no cover
