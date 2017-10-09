#!/usr/bin/env python

from .mqtt_base import MQTTBase


class Publisher(MQTTBase):
    def __init__(self):
        super().__init__()

    def publish(self, topic, content):
        self.mqtt_client.publish(topic, content)


if __name__ == '__main__':
    p = Publisher()
    print('Publishing test data')
    p.block_until_connect()
    p.publish('hello/world', 'this is hello world test')
    p.run_forever()
