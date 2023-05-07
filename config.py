# Using dotenv to use environment variables
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
env = os.environ

timezone = 'Asia/Tehran'
api_id = env["API_ID"]
api_hash = env["API_HASH"]
