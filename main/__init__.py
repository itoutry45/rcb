#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "19802104")
API_HASH = config("API_HASH", "6be78ddee47c08e9ef348d5b2fc6bd84")
BOT_TOKEN = config("BOT_TOKEN", "5689294860:AAHxa7B3ULv8wjcUJpBTr6YiR_3CLtpvsTk")
SESSION = config("SESSION", "BQAyIxLV8JK8c7OV1n5C-NY_rCmE5c6S2nHGnN0SLDZN78i5EqjrwJGzGeGdjVNIC2dEFPSDg7AGZRwHweMhBXyusCRKre4J22A10ajkhAxIMezAkbclpX7INXPKRYqvzQ16bEOWGAQQ-us4XGdApy778fzOJGOvXAWmM3-0M1c3sSuDN37MJpTeayc76VX6qbyaLgeHP7ZeYmOAU1xY0akMWsdL0kzfWKlcX341HUvZ_gkjSVbzO56anVRCTLoUNXAl6ih-Br7nhz5Vgxg77fn9dya87YL3wAR-Y0ZCSRVSQ0F9IQuBxAB9iqjMg05ySRBwEnsocOxg-lwqggwN2Rn9AAAAAT-RHTgA")
FORCESUB = config("FORCESUB", "rcb2_b")
AUTH = config("AUTH", "5361442104")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
