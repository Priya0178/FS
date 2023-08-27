# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', "11948995"))
    API_HASH = str(getenv('API_HASH', "cdae9279d0105638165415bf2769730d"))
    BOT_TOKEN = str(getenv('BOT_TOKEN',"5760032873:AAFrwu8-eEQEBEB5EWzmJ4GgIZSvJid5ebc"))
    name = str(getenv('name', "filetolinkbot"))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', "60"))
    WORKERS = int(getenv('WORKERS', "4"))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', "-1001973449555"))
    PORT = int(getenv('PORT', "8080"))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', "143.244.138.43"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1092802988").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', "legend_x01"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', "143.198.101.144:8080")) if not ON_HEROKU or getenv('FQDN',"143.198.101.144:8080") else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://priyajat427:6tQUH9bax9Lc1rDM@cluster0.0rnwefv.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
