from pyrography import filters
from services.database import async_session
from services.utils import rolar
from RPGBot import RPGBot
import re


@RPGBot.on_message(filters.command('d'))
async def dado(client, message):
    dgex = re.compile(r'(\d+)d(\d+)')
    dados = dgex.findall(message.text)
    resultados = rolar(int(dados[0][0]), int(dados[0][1]))
    template = "Dado {}: {}\n"
    await message.reply("".join(template.format(i + 1, n) for i, n in enumerate(resultados)))
