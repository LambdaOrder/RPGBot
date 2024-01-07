from pyrography import Client
from services.envvars import API_ID, API_HASH, BOT_TOKEN


class RPGBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            name="LambdaOrderRPGBot",
            api_id=API_ID,
            plugins={"root": "plugins"},
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
        )
        self.load_plugins()
