## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCZGanrb_e8QybKQ4HmC27r4SqvjzKvIhqOzMXtwTXtILLr_vJkBx8-JcPPKVW0bqMiHhbGLDbfitzmzQEXqZE49MXiN-jgbRY23EhrVFE5801ZEjtGhEPNYQ8H-YI2JjPd8lZSG0s4BsTfctS0FTCnx0sBphIVfl-m3S-_A43f6g90mX94koemUBLf2Gnd6QSRogMU6U9C1lagK-rzoXquH1htTzNb5sI8F-snlwmREkd0chJBfQsI0b-qpRcDFZaoFG9JHK4wYiylNsbF_FTdZQrRIzq3jko4wCYuzM82hn1wS-zFSvhsl6W3ilyJK6SiPshw0f6226OutwbctsQoAAAAATWvjxgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5523871023:AAEvaTucsLScEc6Vmv22snfhqjQryCUMu_4")
BOT_NAME = getenv("BOT_NAME", "lisa")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "تگسن")
OWNER_USERNAME = getenv("OWNER_USERNAME", "T_T_X_N")
ALIVE_NAME = getenv("ALIVE_NAME", "تگسن")
BOT_USERNAME = getenv("BOT_USERNAME", "llisaMucikbot")
OWNER_ID = getenv("OWNER_ID", "5244755240")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "LDDDA")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "N1111V")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "N1111V")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5244755240").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
