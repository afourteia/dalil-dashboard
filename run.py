import os
from application import create_app
from application.models import User


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == "__main__":
    app.run(debug=True)
