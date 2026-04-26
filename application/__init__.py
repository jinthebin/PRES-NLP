import os
from flask import Flask
from dotenv import load_dotenv

# load environment variables
load_dotenv()

app = Flask(__name__)


app.secret_key = os.getenv('SECRET_KEY', 'default-dev-key-for-emergencies')

from application import routes