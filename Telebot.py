from telegram import Bot
import asyncio
import sys


class Telebot:
    _bot_id = ""
    _chat_id = ""
    _bot = None

    def __init__(self):
        with open("../bot_info.info", "r") as f:
            file_lines = f.readlines()
            self._bot_id = file_lines[0].strip()
            self._chat_id = file_lines[1].strip()

        self._bot = Bot(token=self._bot_id)

    def send_message(self, name, error=False):
        message = ""

        if error:
            message = "Error occurred while taking screenshot for {}".format(name)
        else:
            message = "{}".format(name)

        if self._bot is None:
            self.initialize()

        # asyncio.run(self._bot.send_message(chat_id=self._chat_id, text=message))

    def send_error(self, contents):
        contents = "Error occurred: {}".format(contents)

        if self._bot is None:
            self.initialize()

        # asyncio.run(self.bot.send_message(chat_id=self.chat_id, text=contents))
