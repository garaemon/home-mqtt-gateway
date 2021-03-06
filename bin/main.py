#!/usr/bin/env python

import logging
import logging.config
import os
import sys

from flask import Flask

# setup logger
logging.config.fileConfig(os.path.join(os.path.dirname(__file__), '..', 'logging.conf'))
logger = logging.getLogger()

# add load path to ../home_mqtt_gateway
if __name__ == '__main__':
    libdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    if os.path.exists(os.path.join(libdir, 'home_mqtt_gateway')):
        sys.path.insert(0, libdir)

from home_mqtt_gateway.app import App
from home_mqtt_gateway.ifttt import run_ifttt_webhook

server = Flask(__name__)
app = App()

for c in app.simple_commands:
    logger.info('Registering url for %s' % c.route)
    server.add_url_rule(
        c.route, c.route, app.generate_callback_function_for_simple_command(c), methods=[c.method])
    # app.generate_callback_function_for_simple_command(c))
app.register_passthrough(server)

if __name__ == '__main__':
    run_ifttt_webhook('Running https->mqtt server')
    server.run(host='0.0.0.0')
