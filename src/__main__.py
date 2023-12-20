import re
from pyrography import filters
import services.utils
from services.telegramapi import app
from pyrography.types import InlineKeyboardMarkup, InlineKeyboardButton
from services.database import session



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
