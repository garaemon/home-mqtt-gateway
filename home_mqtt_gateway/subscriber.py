#!/usr/bin/env python

from .mqtt_base import MQTTBase


class Subscriber(MQTTBase):
    def __init__(self):
        super().__init__()

    def subscribe(self, topic, callback):
        self.mqtt_client.on_message = callback
        self.mqtt_client.subscribe(topic)

    def echo_back_callback(self, client, userdata, message):
        print('topic=%s, message=%s' % (message.topic,
                                        str(message.payload)))


if __name__ == '__main__':
    s = Subscriber()
    print('Subscribing test data')
    s.subscribe('hello/world', s.echo_back_callback)
    s.run_forever()
