from app import app
import os

app.config.from_object(os.environ['APP_SETTINGS'])

if __name__ == '__main__':
    app.run()