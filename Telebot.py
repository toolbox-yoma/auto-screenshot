from telegram import Bot
import asyncio
import threading
import sys


class Telebot:
    def __init__(self):
        self._bot_id = ""
        self._chat_id = ""
        self._loop = asyncio.new_event_loop()

        with open("../bot_info.info", "r") as f:
            file_lines = f.readlines()
            self._bot_id = file_lines[0].strip()
            self._chat_id = file_lines[1].strip()

        self._bot = Bot(token=self._bot_id)

    async def _send_async(self, message):
        try:
            await self._bot.send_message(chat_id=self._chat_id, text=message)
        except Exception as e:
            print(f"Error sending message: {e}")

    def _send(self, message):
        def run_coroutine():
            asyncio.set_event_loop(self._loop)
            self._loop.run_until_complete(self._send_async(message))

        thread = threading.Thread(target=run_coroutine)
        thread.start()

    def send_message(self, name, error=False):
        message = ""

        if error:
            message = "Error occurred while taking screenshot for {}".format(name)
        else:
            message = "{}".format(name)

        self._send(message)

    def send_error(self, contents):
        contents = "Error occurred: {}".format(contents)
        self._send(contents)
