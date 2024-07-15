import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("22699294"))
API_HASH = getenv("995abb1f6386e31f212cc00512432072")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6989089257:AAEellMiqcrbYA46Vcw-shGEB4aP0mPcmfw")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = int(getenv("15"))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002166452042"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("5970227997"))

UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
GIT_TOKEN = getenv("GIT_TOKEN")

SUPPORT_CHANNEL = getenv("Zuanel")
SUPPORT_CHAT = getenv("ZuanelDuyuru")

AUTO_LEAVING_ASSISTANT = bool(getenv("False"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT"))

STRING1 = getenv("1BJWap1sBu1DmtUp1E0SEYy04TeV9h-T63LRNN6GwUl4hJpiNGiST111gQX5sSBE5skrdzwlERbAE2WkwkK2k63EM9Rkfa6BoY-J5c7a0Lg2g7Uttmvh1_JSW7-TxJbelSwZRJgtxAsA9lWwH0Co2bAS24n6PVVJ5RFKWQvJ6lZeLEgkiWTHHcW-dmUHptpHGBNsKGv5xGoCK6EZGNw20aT8-6lVEEmM9lycxKXIhgWpIrpnKMZ-JuVCrPNn30i8Xg_yKGsquH_HjeLtdh46w5wbK1n5TlQx02QVfiubadReOH8Wjvt13V9ItgLP_TeWhhODQBYvT9RMDhSLBkmGwqij7DjOUbDo=")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg")
PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STATS_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STREAM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
