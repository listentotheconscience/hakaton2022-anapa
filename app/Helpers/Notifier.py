import requests


class Notifier:
    BASE_URL = 'http://127.0.0.1/notify'

    @classmethod
    def notify(cls, accident_data):
        # Need to send notification request to server
        return accident_data
