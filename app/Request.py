import requests


class Request:
    @classmethod
    def send_notification_to_backend(cls, id, type, status, file):
        form = {
            'id': id,
            'type': type,
            'status': status,
            'file': file
        }