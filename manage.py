from app import create_app
from flask_migrate import Migrate  # migration to the database
from app.models import db
from flasgger import Swagger


app = create_app()

swagger = Swagger(app, template={
    "info": {
        "title": "Inventory API",
        "description": "A simple API to manage inventory",
        "contact": {
            "responsibleOrganization": "Edward Mansour",
            "responsibleDeveloper": "Edward Mansour",
            "email": "",
            "url": "",
        },
        "version": "0.0.1"
    }
})

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
