from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

class Zaid(object):
        admins = {}
        BOT_TOKEN = getenv("BOT_TOKEN", None)
        API_ID = int(getenv("API_ID", "6"))
        API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
        SESSION_NAME = getenv("SESSION_NAME", None)
        DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
        SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
        ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zaid_Video_Assistant")
        BOT_USERNAME = getenv("BOT_USERNAME", "Zaid_VD_BOT")
        COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
        CHANNEL_NAME = getenv("CHANNEL_NAME", "Zaid_Updates")
        GROUP_NAME = getenv("GROUP_NAME", "Zaid_Support")
        OWNER_NAME = getenv("OWNER_NAME", "Timeisnotwaiting")
