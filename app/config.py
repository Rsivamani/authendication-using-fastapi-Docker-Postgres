from dotenv import load_dotenv
import os

load_dotenv()

JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]

DB_CONFIG = {
    "host": os.environ["DB_HOST"],
    "port": os.environ["DB_PORT"],
    "database": os.environ["DB_NAME"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
}

