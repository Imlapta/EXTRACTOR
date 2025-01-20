"""
from os import getenv


API_ID = int(getenv("API_ID", "3737117"))
API_HASH = getenv("API_HASH", "f466ca6ff400954d192ce0992ddf8b5d")
BOT_TOKEN = getenv("BOT_TOKEN", "1794688698:AAFDoYKCbL5xHgduCK6sOQKaUC7P17L3UvU")
OWNER_ID = int(getenv("OWNER_ID", "1110590703"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6050277919 2112898623").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://rrahuldhaker:7F6evbaKu8m7Ybr5@cluster0.w5kvs.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002247262105"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002247262105"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

