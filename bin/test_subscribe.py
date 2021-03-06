#!/usr/bin/env python

import os
import sys

# add load path to ../home_mqtt_gateway
if __name__ == '__main__':
    libdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    if os.path.exists(os.path.join(libdir, 'home_mqtt_gateway')):
        sys.path.insert(0, libdir)

from home_mqtt_gateway.subscriber import Subscriber
from home_mqtt_gateway.app import SIMPLE_COMMANDS

if __name__ == '__main__':
    s = Subscriber()
    for c in SIMPLE_COMMANDS:
        s.subscribe(c.topic, s.echo_back_callback)
    s.run_forever()
