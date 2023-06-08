import os
import requests as rq


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.TWILLIO_SID = os.environ.get("TWILLIO_SID")
        self.TWILLIO_TOKEN = os.environ.get("TWILLIO_TOKEN")
    pass
