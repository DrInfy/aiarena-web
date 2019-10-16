import json

from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer
from ..core.models import Result, Match
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    # def receive(self, text_data=None, bytes_data=None):
    def receive(self, text_data, **kwargs):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))


class ArenaclientConsumer(JsonWebsocketConsumer):
    """
    Websocket consumer for arena clients to maintain a live connection with the website.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_layer = get_channel_layer()
        self.match_id = self.scope['url_route']['kwargs']['match_id']

    def connect(self):
        # todo: auth
        # todo: verify the AC is the one assigned to this match
        self.accept()
        async_to_sync(self.channel_layer.group_add)(str(self.match_id), self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(str(self.match_id), self.channel_name)

    def receive(self, text_data=None, bytes_data=None, **kwargs):
        pass

    def cancel_match(self, event):
        self.send_json(event['data'])

    @staticmethod
    @receiver(post_save, sender=Result)
    def result_signal_handler(sender, instance, **kwargs):
        if instance.type == 'MatchCancelled':
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                str(instance.match.id),
                {
                    'type': 'cancel_match',  ## cancel_match function
                    'data': {
                        'result': instance.type
                    }
                }
            )
