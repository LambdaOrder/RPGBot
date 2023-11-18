from os import getenv
from dotenv import load_dotenv
from pyrography import Client, filters
from asyncio import run

load_dotenv()
api_hash = getenv("api_hash")
api_id = getenv("api_id")
bot_token = getenv("bot_token")
app = Client("LambdaOrderRPGBot", api_id=api_id,
                api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command('start'))
async def messages(client, message):
    await message.reply("Hello world")

app.run()
