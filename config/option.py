import sys, os
import config, json5
import getopt, logging
from wechat.chatroom import ChatRoomConfig

def get_app_config():
    # 应用配置
    app_config = dict()
    config_file = 'config.json'
    opts = getopt.getopt(sys.argv[1:], 'c:', longopts=['config='])
    for item in opts:
        if len(item) == 0:
            continue
        item = item[0]
        key = item[0]
        if key == '-c' or key == '--config':
            config_file = item[1]
    if not os.path.exists(config_file):
        raise Exception('无法找到配置文件：%s' % config_file)
    # 加载配置文件
    with open(config_file, 'r', encoding=config.UTF8_ENCODING) as f:
        try:
            app_config = json5.load(f)
        except Exception as ex:
            raise Exception('无法加载配置文件：%s' % str(ex))
    return app_config

def apply_app_config(app_config):
    config.ENABLE_LOGIN = app_config['ENABLE_LOGIN']
    config.ENABLE_POST_URL = app_config['ENABLE_POST_URL']
    config.ENABLE_SHOW_SOURCE = app_config['ENABLE_SHOW_SOURCE']
    config.ENABLE_PUSH_MSG = app_config['ENABLE_PUSH_MSG']
    config.TASK_INTERVAL = app_config['TASK_INTERVAL']
    config.CONSOLE_CMD_QR = app_config['CONSOLE_CMD_QR']
    chatrooms = []
    for chatroom_config in app_config['MSG_PUSH_CONFIG']:
        # 忽略示例
        if chatroom_config['NICK_NAME'] == '$CHATROOM_NAME':
            continue
        chatrooms.append(get_chatroom(chatroom_config))
    # 更新推送消息设定
    config.MSG_PUSH_CONFIG = chatrooms

def get_chatroom(chatroom_config):
    nick_name = chatroom_config['NICK_NAME']
    user_name = ''
    if 'USER_NAME' in chatroom_config.keys():
        user_name = chatroom_config['USER_NAME']
    # 获取已获取的群聊user_name
    user_mapping = dict()
    for item in config.MSG_PUSH_CONFIG:
        user_mapping[item.nick_name] = item.user_name
    if nick_name in user_mapping.keys():
        user_name = user_mapping[nick_name]
    msg_enable = chatroom_config['MSG_ENABLE']
    keyword = dict()
    for resource in chatroom_config['KEYWORD']:
        resource_config = chatroom_config['KEYWORD'][resource]
        keyword[resource] = dict()
        for key in ['INCLUDE', 'EXCLUDE', 'MALLS', 'NONMALLS']:
            if key not in resource_config.keys():
                continue
            keyword[resource][key.lower()] = resource_config[key]
    return ChatRoomConfig(nick_name=nick_name, user_name=user_name, msg_enable=msg_enable, keyword=keyword)

def auto_app_config():
    app_config = get_app_config()
    apply_app_config(app_config)
