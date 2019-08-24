# -*- coding: utf-8 -*-
import json
import requests
import config


def get_resp(url, headers=None):
    return requests.get(url, headers=headers, timeout=config.REQUEST_TIMEOUT)

def get_resp_json(url, params=None):
    resp = requests.get(url, params=params, timeout=config.REQUEST_TIMEOUT)
    if resp.status_code == 200:
        try:
            return json.loads(resp.text, strict=False)
        except Exception as ex:
            raise Exception('call json.loads error: %s, response: %s' % (str(ex), resp.text))
    else:
        raise Exception('request error: %s, url: %s' % (resp.status_code, url))