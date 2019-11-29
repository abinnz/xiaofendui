# 是否开启登陆
ENABLE_LOGIN = True
# 是否推送消息
ENABLE_PUSH_MSG = True
# 消息是否带上链接
ENABLE_POST_URL = True
# 消息是否带上来源
ENABLE_SHOW_SOURCE = False
# 控制台二维码设定，值为1或者2，部分系统需设定为1
CONSOLE_CMD_QR = 1

# 不合并图片的最大数量，默认自动合并多张图片
ALLOW_MAX_IMAGE_COUNT = 1
# 请求超时设置，默认10秒
REQUEST_TIMEOUT = 10
# 任务间隔时间
TASK_INTERVAL = 30

# 编码
UTF8_ENCODING = 'utf-8'
GBK_ENCODING = 'gbk'
GB2312_ENCODING = 'gb2312'
GB18030_ENCODING = 'gb18030'

# 存储目录
BASE_TMP_DIR = 'tmp'

# 请求头
REQUEST_HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
MOBILE_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36'
}

# 消息推送设定
MSG_PUSH_CONFIG = []