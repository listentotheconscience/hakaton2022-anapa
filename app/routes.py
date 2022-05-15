from app import app, mock_data
from .Helpers.json import response_success, response_failed
from .Helpers.Notifier import Notifier
import random

# Need to get data from ML
data = mock_data.get_mock_data()


@app.route('/status/<int:camera_id>')
def status(camera_id: int):
    statuses = list(filter(lambda item: item['camera_id'] == camera_id, data))
    return response_success(Notifier.notify(random.choice(statuses) if statuses else []))