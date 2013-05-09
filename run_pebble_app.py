#!/usr/bin/env python

from claypellet.harness import PebbleHarness
from claypellet.display import PebbleDisplay


ph = PebbleHarness('build/claypellet_app.so', 'build/app_resources.pbpack')
pd = PebbleDisplay(ph)
pd.run()
