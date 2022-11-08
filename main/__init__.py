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
SESSION = config("SESSION", "BQDCwZSSVb1L4MPMZZsrnCdZ584P8d24sYrrc5rc8dooVTVQf8aU0CboF6pMQLUGNj8pGZr4feDTCbOgc6voXpaczZnsP0IXCxOttO0zxPcMm4qAD09Q1EnhO4lPNLTnhvEj0rzwMlRCYUv9jS4hcuW0fbN8ILeMwBnLwU1jR2uM26tepNq9Xwgw6GMTFy0Nw73S7teyozbV3GC8YRyO8dGW9W14MtZkUL6AYl3qpK_-tIoyZ2o4PJaUj1bE_Y0TiW1cjUCKLxYp0H8dPxSzlgPfTuAiufOPNkQn3D3G7-5aOxw7vVrMbE4RWPYx9fg5WYZ1pE8p5ccE3XTJV4PXaF4XAAAAAT-RHTgA")
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
