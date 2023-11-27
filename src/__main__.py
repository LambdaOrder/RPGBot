from os import getenv
import re
from dotenv import load_dotenv
from pyrography import Client, filters
from asyncio import run
import utils

load_dotenv()
api_hash = getenv("API_HASH")
api_id = getenv("API_ID")
bot_token = getenv("BOT_TOKEN")
app = Client("LambdaOrderRPGBot", api_id=api_id,
             api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command('d'))
async def dado(client, message):
    dgex = re.compile('(\d+)d(\d+)')
    dados = dgex.findall(message.text)
    resultados = utils.rolar(int(dados[0][0]), int(dados[0][1]))
    template = "Dado {}: {}\n"
    await message.reply("".join(template.format(i + 1, n) for i, n in enumerate(resultados)))


@app.on_message(filters.command('start'))
async def messages(client, message):
    await message.reply("Hello world")


if __name__ == "__main__":
    app.run()
