import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    BOT_TOKEN = os.getenv("7548879127:AAGn6vgGmKpDlSCNNxH7m4mLBeP2lwkIhE4")
    API_ID = os.getenv("25373607")
    API_HASH = os.getenv("3b559c2461a210c9654399b66125bc0b")
    DB_HOST = os.getenv("66.118.245.28")
    DB_USER = os.getenv("root")
    DB_PASSWORD = os.getenv("tHR16SZyr81n0z6GFx")
    DB_NAME = os.getenv("Alevps")
