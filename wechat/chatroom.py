# -*- coding: utf-8 -*-
import json
import wechat
import logging

'''
微信群聊，消息推送设定
'''
class ChatRoomConfig(object):

    def __init__(self, nick_name, msg_enable=False, user_name='', pic_enable=True, 
                    global_keyword=None, keyword=None, disable_talking=False, strict=False):
        # 严格：要求匹配关键字和商城
        self.strict = strict
        self.nick_name = nick_name
        self.user_name = user_name
        self.disable_talking = disable_talking
        # 是否接受消息
        self.msg_enable = dict()
        # 是否允许发送图片
        self.pic_enable = pic_enable
        # 默认所有群聊不推送
        if type(msg_enable) is type(True):
            self.msg_enable = msg_enable
        elif type(msg_enable) is type([]):
            self.msg_enable = msg_enable
        # 全局关键关键字
        self.global_keyword = None
        if type(global_keyword) is type(dict()):
            self.global_keyword = wechat.get_keyword(global_keyword)
        # 爬取源关键字
        self.keyword = None
        if type(keyword) is type(dict()):
            self.keyword = dict()
            for key in keyword.keys():
                self.keyword[key] = wechat.get_keyword(keyword[key])

    # 是否屏蔽推送
    def enable_push(self, post_detail):
        # 设置全局消息内容
        if self.global_keyword:
            return self._enable_push(post_detail, self.global_keyword, '全局')
        if not self.keyword or post_detail.source not in self.keyword.keys():
            return True
        # 消息源
        return self._enable_push(post_detail, self.keyword[post_detail.source], post_detail.source)

    # 是否推送
    def _enable_push(self, post_detail, keyword, group_name):
        result = wechat.enable_push_content(keyword, post_detail.content)
        mall_result = wechat.enable_push_mall(keyword, post_detail.mall)
        if not result and not mall_result:
            result_type = '' if result else '【内容】'
            result_type += '' if mall_result else '【商城】'
            logging.info('消息%s屏蔽，规则严格：%s，【%s】规则：%s' % (result_type, self.strict, group_name, str(keyword)))
        return result and mall_result if self.strict else result or mall_result

    # 群聊是否推送
    def enable_chatroom_push(self, source):
        if type(self.msg_enable) is type(True):
            return self.msg_enable
        if type(self.msg_enable) is type([]):
            return source in self.msg_enable
        return False

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)
