import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    BOT_TOKEN = os.getenv("7548879127:AAGn6vgGmKpDlSCNNxH7m4mLBeP2lwkIhE4")
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
