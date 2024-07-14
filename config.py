import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT"))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID"))

UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
GIT_TOKEN = getenv("GIT_TOKEN")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")
SUPPORT_CHAT = getenv("SUPPORT_GROUP")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT"))

STRING1 = getenv("STRING_SESSION")
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

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://t.me/Zuanel", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match(r"(?:http|https)://t.me/ZuanelDuyuru", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
        {
  "builds": [
    {
      "src": ".",
      "use": "docker"
    }
  ],
  "deployments": [
    {
      "src": ".",
      "use": "@railway/with-docker",
      "env": {
        "API_ID": "24445445",
        "API_HASH": "147f032d190ffc3bef9e0ab4c1dafc3a",
        "BOT_TOKEN": "6984331915:AAHKISC-JqFpxX0QXrdkuhRBDX1MT7Tj1VE",
        "MONGO_DB_URI": "mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority",
        "DURATION_LIMIT": "500",
        "LOGGER_ID": "-1002248089351",
        "OWNER_ID": "5970227997",
        "UPSTREAM_REPO": "https://github.com/Learningbots79/LB_Music",
        "UPSTREAM_BRANCH": "master",
        "GIT_TOKEN": "",
        "SUPPORT_CHANNEL": "https://t.me/ZuanelDuyuru",
        "SUPPORT_GROUP": "https://t.me/Zuanel",
        "AUTO_LEAVING_ASSISTANT": "False",
        "SPOTIFY_CLIENT_ID": "",
        "SPOTIFY_CLIENT_SECRET": "",
        "PLAYLIST_FETCH_LIMIT": "25",
        "TG_AUDIO_FILESIZE_LIMIT": "104857600",
        "TG_VIDEO_FILESIZE_LIMIT": "1073741824",
        "STRING_SESSION": "1BJWap1sBuw13sl-hiBhRVH9_yf6i3vIpsDShXZ8GDHElweyDRawf2qWVa9KPQoEl_4vLoyVbSbfJJQYGF7DEBttH_24iIWrnfxOxTimmmdMkDjhmfryVZqT7B_24V5P3yGADfDd9bz4SADbNNOBvK7xz15-X9q3y6X1_Z7kv_mJkaqIXCSsT7zJNKvBXTOlc8HRdG76PLQuRGNF9ec7retTSm7bA67pSzNGOb0SDhB5VjqkzxzRpebvRXY7Vn9Loj5vcRqEqls4WUToNP_muV7ESgVp-m8a7IMlKArvwbzsOkXhFa4NNLOZCxaHhmEwGg66XlfWFtFuAMho08fXWMKpIc5LFA44=",
        "STRING_SESSION2": "",
        "STRING_SESSION3": "",
        "STRING_SESSION4": "",
        "STRING_SESSION5": ""
      }
    }
  ]
}
