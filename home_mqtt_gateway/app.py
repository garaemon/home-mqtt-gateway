#!/usr/bin/env python

from .publisher import Publisher


class App(object):
    def __init__(self):
        self.publisher = Publisher()

    def block_until_connect(self):
        self.publisher.block_until_connect()

    def publish_message_with_html_result(self, topic, content):
        self.publisher.publish(topic, content)
        return 'Published message to %s' % topic

    def callback_for_route(self):
        return self.publish_message_with_html_result(
            'hello/world', 'hello world sentence')
