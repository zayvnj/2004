from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")
BOT_TOKEN = getenv("BOT_TOKEN", "6164782519:AAEs5lDxD2n4zQYe6XpUcjb1taDZPvWUt5w")
SESSION_NAME = getenv("SESSION_NAME", "BAB3X0ypbnd_iUTKkOVnHYVgSjAQ_ZMu_dh8LSutCa0vIJfv-C7dIPinq3U-FRXE2tVSOv8KaAgWxMEbmJQ0dBiosxQloAMBAcJ8ULLfmKEpiC41rT3SqXnrNpcKd6dyle2ZLOQM8y_W1spcqstfVf2CPWmTwFuWaHj6jRXv0v7JTK3O6KYqinjI42UgtqLsbPCfew9h4EhyE56FmwKWxZHV4hXKAIAOXPkwTENotWGGrBYuOe5Ar1D9rOKDTJSTKt4sPBf2ttIsUWsHdnS8A89bmBwtc6u1G3ytag5Mm7EMa7kfiTJ9HC3jLTJ0mHGcldITK4VyQSM3T9HoD2Jvn3QEAAAAAXFnGG8A")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "gfyfjbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "zain1zv")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "zain1zv")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5630438698").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5630438698").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
