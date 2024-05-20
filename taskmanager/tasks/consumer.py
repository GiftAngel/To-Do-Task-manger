from channels.generic.websocket import WebsocketConsumer
import json

class DataStreamConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Process the received message and send the real-time data back to the client
        data = {'message': 'Real-time data: ' + message}
        self.send(text_data=json.dumps(data))