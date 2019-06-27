from time import sleep

import requests

from settings import TOKEN


class BotError(Exception):
    pass


class MessageBot:
    URL = f"https://api.telegram.org/bot{TOKEN}/"

    def _get(self, method, params=None):
        return requests.get(self.URL + method, params, timeout=5).json()

    def _post(self, method, data=None):
        return requests.get(self.URL + method, json=data, timeout=5).json()

    def get_chat_ids(self):
        updates = self._get('getUpdates')
        if not updates or not updates.get('result'):
            raise BotError('Не удалось выполнить запрос в телегу')
        return {x['message']['chat']['id'] for x in updates['result']}

    def send_message_to_chats(self, message):
        for chat in self.get_chat_ids():
            self._post('sendMessage', {'chat_id': chat, 'text': message})
            sleep(1.1)


if __name__ == '__main__':
    b = MessageBot()
    b.send_message_to_chats('Проверка')
