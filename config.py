import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("25345631"))
API_HASH = getenv("892caa6c1594b799e0b66e3182398dbf")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7334778726:AAFDjpfAlyrp2UKcqDC9MTzm0B_W7ixKSUc")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://modsandy34:Samet01@zuanel.ymhwsh4.mongodb.net/?retryWrites=true&w=majority&appName=Zuanel")

DURATION_LIMIT_MIN = int(getenv("15"))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("1002142859371"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("5970227997"))

UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
GIT_TOKEN = getenv("GIT_TOKEN")

SUPPORT_CHANNEL = getenv("Zuanel")
SUPPORT_CHAT = getenv("ZuanelDuyuru")

AUTO_LEAVING_ASSISTANT = bool(getenv("False"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID",None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET",None)

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT"))

STRING1 = getenv("1BJWap1sBu2lv-Pc27-MgMrOuz2Q1Qgapzx1R3xOn-BIr5yJOZ8BAgFuvtyp0IiuVAwW9j6aKtmtt-vLVXL-XacgMk3kiHsAnm26gfmBnWRK6VjxFmM0_BYfUDSpv2H9UueIFHkU0ITKfdT14OvgGeH1VCke0IhlCLuHeJeSFzumITGMLjtFRHWj2qGXObd5ZtaCbgUvzxTG5I2DGdWwJEasPGBKJFjHtfR5s21YlTc6TRkFw-Dr-YM8CYXAtohf6SOwDUxAWCi36t3ML_XmZj-YGu2qKtT8h2eKdNGflDwOQuyk5JcS2y_JkiCvVax-eGjv4COPA-ZdTfkVPmwb9BObo1Xq13Ks=")
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
