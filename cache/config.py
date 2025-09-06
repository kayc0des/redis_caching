# Declare Environment Variables
import os
from dotenv import find_dotenv, load_dotenv

try:
    load_dotenv(find_dotenv())
except Exception as e:
    print(f"Exception Caught: {e}")

class Settings():
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")
    REDIS_DB = os.getenv("REDIS_DB")