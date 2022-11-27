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
SESSION = config("SESSION", "BQDE8YBhIhzYNKfO3XlH2NgPew5GPp6vNbF0UtuHVB79qqe8vrdLSOR-6tEXGrDIqtIOEDLp2JteQS07EpmdvfZma6FYvp32SINTlgKLVd8zh4iLA4T0ZnrMI8G18SUx36j5kUqnMNQBtUh-8JRr6dhyhTABkj_Y4L7q79v82u7Rn1u3GYh29kc2s9PdRIPG2uRlByGGd6m84lTw9CRkXUE4CFLMHgVFWpaDBrOQE1wmZoB21vvrFCGLf-ZUwyPpevJrUX-cPqryy0QBuaWki78IUSNsSCP_3A67ZzppmXVd5hd0T2PfjkgfjxHHX5ete0wROuErIgHXtEjDipz9ARIPAAAAAT-RHTgA")
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
