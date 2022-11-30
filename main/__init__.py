#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 19802104
API_HASH = "6be78ddee47c08e9ef348d5b2fc6bd84"
BOT_TOKEN = "5689294860:AAHxa7B3ULv8wjcUJpBTr6YiR_3CLtpvsTk"
SESSION = "BQB6JIa99tQvo7GItKUKq0_wm2a6Ul7T1p_Fogv7lNImSfj69x_p0ROWgMROsnAoGCEATGAIlPFtF07_ptUpHMDbVERtUxNpsU6QVn6eKCQq4e0v0mH65sGmPoldYBPM6MN4ROPtBjqSiqe4uGpDxAIU_W5s1ODKVDfoZ5l_pARcUfQDjvwjc1UyKZenBJrY9R_zhzygt_HaTnQ9iuauFt2cc0P1pbVu5MBGnz3sXoscxj96b7nTG1kqSeqw_wq8YWjTAceNmBUbWxMiE3MncHjdJuZ3szRenN3F-eUmpVbeUPz16QfJMixh0k8ISrXQ5MfaJ7RezkoJ4vladYgO47aJAAAAAT-RHTgA"
FORCESUB = "rcb2_b"
AUTH = 5361442104

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
