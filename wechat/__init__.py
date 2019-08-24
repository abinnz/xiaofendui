# -*- coding: utf-8 -*-
import re

'''
是否推送内容
exclude优先于include
'''
def enable_push_content(keyword, content):
    include_list = re.findall(keyword['include'], content, re.I)
    exclude_list = []
    if keyword['exclude'] is not None:
        exclude_list = re.findall(keyword['exclude'], content, re.I)
    if len(include_list) == 0 or len(exclude_list) > 0:
        return False
    else:
        return True

'''
是否推送商城
nonmalls优先于malls
'''
def enable_push_mall(keyword, mall):
    if mall in keyword['nonmalls']:
        return False
    if mall in keyword['malls']:
        return True
    return False

'''
获取关键字
'''
def get_keyword(keyword):
    obj = dict()
    if 'include' not in keyword.keys():
        obj['include'] = '.*'
    else:
        obj['include'] = keyword['include']
    if 'exclude' not in keyword.keys():
        obj['exclude'] = None
    else:
        obj['exclude'] = keyword['exclude']
    if 'malls' not in keyword.keys():
        obj['malls'] = []
    else:
        obj['malls'] = keyword['malls']
    if 'nonmalls' not in keyword.keys():
        obj['nonmalls'] = []
    else:
        obj['nonmalls'] = keyword['nonmalls']
    return obj