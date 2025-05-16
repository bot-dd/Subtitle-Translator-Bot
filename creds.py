import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred:
    BOT_NAME = os.getenv("BOT_NAME", "subtr")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7560563197:AAHmmIygYMElUtUPnYc2Iu05v5y1KOTWpnY")  # From botfather
    API_ID = os.getenv(
        "26649585"
    )  # "Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv(
        "588a3ea6fd01ae88bd2e10fed7d55b2c"
    )  # "Get this value from my.telegram.org! Please do not steal"
    DB_URL = os.getenv("mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")  # From Firebase database
