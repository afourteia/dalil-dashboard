import os
from application import create_app, db
from application.models import User
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
