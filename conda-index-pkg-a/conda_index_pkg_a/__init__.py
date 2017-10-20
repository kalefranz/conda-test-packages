from __future__ import absolute_import, division, print_function, unicode_literals

import json
import os


def main():
    print(json.dumps(dict(os.environ), indent=2, sort_keys=True,
                     separators=(',', ': ')))


def helper():
    print(json.dumps(dict(os.environ), indent=2, sort_keys=True,
                     separators=(',', ': ')))
