from flask.cli import FlaskGroup
from app import create_app, db

cli = FlaskGroup(create_app=create_app)

@cli.command("create_db")
def create_db():
    db.create_all()

if __name__ == "__main__":
    cli()
