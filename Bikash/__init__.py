import json
import os

from Bikash.core.bot import BikashBot
from Bikash.core.dir import dirr
from Bikash.core.git import git
from Bikash.core.userbot import Userbot
from Bikash.misc import dbb, heroku, sudo

from .logging import LOGGER

# Bot Client

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

app = BikashBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}

TOKEN = {
    "access_token": "ya29.a0AcM612x3BhQYxpwWKVhKrOEibthwGRC5-7fGQgq1Co8g2rFVmD3TyZez5CM05axN7zK7nyPVRsAz_Q03PApFye3hS0OH84s5U0vJ-mpaRCNfgA4cOHAZxBZmWNKm1tnHIma-2oNyRiHNqi9EoepslcOiUEsSQRlnItiemT4Tm10yX3yMJh1HaCgYKAT4SARISFQHGX2MidCZ1bcqwywAZVeQpeKll1Q0187",
    "expires": 1729735521.927958,
    "token_type": "Bearer",
    "refresh_token": "1//05vYI0c8OP0b4CgYIARAAGAUSNwF-L9IrJvP8EzLj-4wkJD-hYD9y1fXRNSGS9CjEQ1YwRxFw1OjatSgXsGooDbs5QcqAPOs3TvM"
}

# Convert TOKEN dictionary to a JSON string
os.environ["TOKEN_DATA"] = json.dumps(TOKEN)
