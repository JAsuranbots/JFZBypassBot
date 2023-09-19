from os import getenv
from time import time
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import ParseMode
from logging import getLogger, FileHandler, StreamHandler, INFO, ERROR, basicConfig
from uvloop import install

install()
basicConfig(format="[%(asctime)s] [%(levelname)s] - %(message)s", #  [%(filename)s:%(lineno)d]
            datefmt="%d-%b-%y %I:%M:%S %p",
            handlers=[FileHandler('log.txt'), StreamHandler()],
            level=INFO)

getLogger("pyrogram").setLevel(ERROR)
LOGGER = getLogger(__name__)

load_dotenv('config.env', override=True)
BOT_START = time()

class Config:
    BOT_TOKEN = getenv('BOT_TOKEN', '6544751534:AAE39MNKeamUdrf2kVFAa7D_yr76paBedmU')
    API_HASH  = getenv('API_HASH', 'fcdc178451cd234e63faefd38895c991')
    API_ID    = getenv('API_ID', '1923471')
    if BOT_TOKEN == '' or API_HASH == '' or API_ID == '':
        LOGGER.critical('ENV Missing. Exiting Now...')
        exit(1)
    AUTH_CHATS      = getenv('AUTH_CHATS', '-1004029598831').split()
    OWNER_ID        = int(getenv('OWNER_ID', '880087645'))
    DIRECT_INDEX    = getenv('DIRECT_INDEX', '').rstrip('/')
    LARAVEL_SESSION = getenv('LARAVEL_SESSION', '')
    XSRF_TOKEN      = getenv('XSRF_TOKEN', '')
    GDTOT_CRYPT     = getenv('GDTOT_CRYPT', '')
    DRIVEFIRE_CRYPT = getenv('DRIVEFIRE_CRYPT', '')
    HUBDRIVE_CRYPT  = getenv('HUBDRIVE_CRYPT', '')
    KATDRIVE_CRYPT  = getenv('KATDRIVE_CRYPT', '')
    UPTOBOX_TOKEN   = getenv('UPTOBOX_TOKEN', '4a4ecf35552fea876da1d63e7fd000d2cb2fo')
    TERA_COOKIE     = getenv('TERA_COOKIE', 'YQOR7exteHuiC7XNl_TAD_ZaXGexSokJJwoblC4S')

Bypass = Client("FZ", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN, plugins=dict(root="FZBypass/plugins"), parse_mode=ParseMode.HTML)
