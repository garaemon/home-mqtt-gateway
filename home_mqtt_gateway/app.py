#!/usr/bin/env python

import logging
import os

from .publisher import Publisher

logger = logging.getLogger()


class SimpleCommandContainer(object):
    def __init__(self, route, topic, content=None):
        self.route = route
        self.topic = topic
        self.content = content


SIMPLE_COMMANDS = [
    SimpleCommandContainer(route='/',
                           topic='hello/world',
                           content='hello world sentence'),
    SimpleCommandContainer(route='/start_cleaning',
                           topic='cleaning/start'),
    SimpleCommandContainer(route='/stop_cleaning',
                           topic='cleaning/sttop'),
    SimpleCommandContainer(route='/turn_on_light0',
                           topic='light0/turn_on'),
    SimpleCommandContainer(route='/turn_on_light1',
                           topic='light1/turn_on'),
    SimpleCommandContainer(route='/turn_off_light0',
                           topic='light0/turn_off'),
    SimpleCommandContainer(route='/turn_off_light1',
                           topic='light1/turn_off'),
    SimpleCommandContainer(route='/turn_on_tv',
                           topic='tv/turn_on'),
    SimpleCommandContainer(route='/turn_off_tv',
                           topic='tv/turn_off'),
    SimpleCommandContainer(route='/volume_up_tv',
                           topic='tv/volume_up'),
    SimpleCommandContainer(route='/volume_down_tv',
                           topic='tv/volume_down'),
    SimpleCommandContainer(route='/channel_up_tv',
                           topic='tv/channel_up'),
    SimpleCommandContainer(route='/channel_down_tv',
                           topic='tv/channel_down'),
    ]


class App(object):
    def __init__(self):
        self.simple_commands = SIMPLE_COMMANDS

    def get_all_routes(self):
        return [c.route for c in self.simple_commands]

    def publish_message_with_html_result(self, topic, content):
        publisher = Publisher()
        publisher.block_until_connect()
        publisher.publish(topic, content)
        publisher.proc(timeout=2.0)
        publisher.disconnect()
        return 'Published message to %s' % topic

    def callback_for_root(self):
        return self.publish_message_with_html_result(
            'hello/world', 'hello world sentence')

    def callback_for_simple_command(self, c):
        logger.info('Run callback for route %s' % c.route)
        return self.publish_message_with_html_result(
            c.topic, c.content)

    def generate_callback_function_for_simple_command(self, c):
        def callback():
            return self.callback_for_simple_command(c)
        return callback
