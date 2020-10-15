# -*- coding:utf-8 -*-
import json

from django.core import serializers


def model_change_json(data_list):
    json_data = serializers.serialize("json", data_list)
    objStr = json.loads(json_data)
    objStr = json.dumps(json_data)
