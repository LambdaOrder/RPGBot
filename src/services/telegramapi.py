from pyrography import Client
from services.envvars import API_ID, API_HASH, BOT_TOKEN
app = Client("LambdaOrderRPGBot", api_id=API_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN)
