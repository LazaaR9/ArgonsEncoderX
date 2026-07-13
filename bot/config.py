# Developed by ARGON telegram: @REACTIVEARGON
import os

from dotenv import load_dotenv

load_dotenv()


# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6877201333:AAG5tomRtBTvjTWoifRz1TC0h4w0KXo3lk8")
# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25918874"))  # Placeholder ID
# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "87c7c525932cf3d753bea33786ad71ee")
# Your db channel Id
LOG_CHANNEL = int(os.environ.get("CHANNEL_ID", "-1001811301225"))  # Placeholder channel ID
# NAMA OWNER
OWNER = os.environ.get("OWNER", "5179011789")
# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5179011789"))  # Placeholder owner ID
# Port
PORT = os.environ.get("PORT", "8030")
# Database
DB_URI = os.environ.get(
    "DATABASE_URL",
    "mongodb+srv://zee:zee@cluster0.s5dgb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",  # Placeholder DB URI
)
DB_NAME = os.environ.get("DATABASE_NAME", "argons")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))
