import requests


class Bot:
    def __init__(self, token):
        self.token = token

        self.url = "https://api.telegram.org/bot{}".format(self.token)

    def get_me(self):
        resp = requests.get(self.url + "/getMe")

        return resp

    def get_updates(self):
        resp = requests.get(self.url + "/getUpdates")

        return resp

    def send_message(self, chat_id, text, parse_mode):
        params = dict(chat_id=chat_id, text=text, parse_mode=parse_mode)

        resp = requests.get(self.url + "/sendMessage", params=params)

        return resp
