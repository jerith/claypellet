#!/usr/bin/env python

from optparse import OptionParser

from claypellet.harness import PebbleHarness
from claypellet.display import PebbleDisplay


DEFAULT_APP = 'build/claypellet_app.so'
DEFAULT_RES = 'build/app_resources.pbpack'


option_parser = OptionParser()
option_parser.add_option("-a", "--app", dest="app", default=DEFAULT_APP,
                         help="Load app from FILE", metavar="FILE")
option_parser.add_option("-r", "--resources", dest="res", default=DEFAULT_RES,
                         help="Load resources from FILE", metavar="FILE")
option_parser.add_option("-f", "--firmware", dest="firmware", default=None,
                         help="Load firmware from FILE", metavar="FILE")

options, _ = option_parser.parse_args()


ph = PebbleHarness(options.app, options.res, options.firmware)
pd = PebbleDisplay(ph)
pd.run()
