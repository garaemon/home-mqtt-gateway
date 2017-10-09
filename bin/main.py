#!/usr/bin/env python

import os
import sys

from flask import Flask

# add load path to ../home_mqtt_gateway
if __name__ == '__main__':
    libdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    if os.path.exists(os.path.join(libdir, 'home_mqtt_gateway')):
        sys.path.insert(0, libdir)

from home_mqtt_gateway.app import App

server = Flask(__name__)
app = App()


for c in app.simple_commands:
    print('Registering url for %s' % c.route)
    server.add_url_rule(c.route, c.route, app.generate_callback_function_for_simple_command(c))
    # app.generate_callback_function_for_simple_command(c))


if __name__ == '__main__':
    app.block_until_connect()
    server.run()
