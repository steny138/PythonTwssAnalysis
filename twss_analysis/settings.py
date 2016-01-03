# -*- coding: utf-8 -*-

import json

SETTINGS = None

class Settings(object):

    """docstring for Settings"""

    def __init__(self, dic):
        super(Settings, self).__init__()
        self.engine_connect = dic['engine_connect']

if __name__ == "settings":
    if SETTINGS is None:
        with open("normal_settings.json") as data_file:
            data = json.load(data_file)

        SETTINGS = Settings(data)
