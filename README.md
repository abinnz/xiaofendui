### 1. 小分队机器人
![xiaofendui](http://wx3.sinaimg.cn/large/800facaagy1g6b1t5p40hj20jy0c4jry.jpg)

### 2. 安装依赖库
```
pip install pillow
pip install requests
pip install json5
pip install itchat
```

### 3. 应用配置
根据自己的推送需求，修改``config.json``配置文件
```
{  
    // 是否开启登陆，必填参数
    "ENABLE_LOGIN": true,
    // 是否推送消息，必填参数
    "ENABLE_PUSH_MSG": true,
    // 消息是否带上链接
    "ENABLE_POST_URL": true,
    // 消息是否带上来源
    "ENABLE_SHOW_SOURCE": false,
    // 控制台二维码设定，值为1或者2，部分系统需设定为1
    "CONSOLE_CMD_QR": 2,
    // 任务间隔时间，必填参数
    "TASK_INTERVAL": 30,
    // 推送消息配置，可配置多个群聊
    "MSG_PUSH_CONFIG": [
        {
            // 示例：群聊名称（建议不带特殊符号），登录前需将群聊保存到通讯录
            "NICK_NAME": "$CHATROOM_NAME",
            // 推送的消息源，为空不推送任何消息
            "MSG_ENABLE": [],
            // 群聊消息推送设定，可选参数，为空消息不过滤
            "KEYWORD": {
                // 对应消息源过滤规则，消息源不设定全部推送
                "RESOURCE_NAME": {
                    // 消息包含关键字，多个参数用“|”，可选参数
                    "INCLUDE": "",
                    // 消息不包含关键字，多个参数用“|”，可选参数
                    "EXCLUDE": "",
                    // 消息包含商城，比如：京东、淘宝、天猫，可选参数
                    "MALLS": [],
                    // 消息不包含商城，比如：京东、淘宝、天猫，可选参数
                    "NONMALLS": []
                }
            }
        }
    ]
}
```

### 4. 启动应用程序
```
# 默认加载目录config.json配置文件
# 命令行可选参数: -c, --config FILENAME
python main.py
```

### 5. 已知问题
1. 如遇控制台显示二维码不正常，请修改 ``config.json`` 配置项 ``CONSOLE_CMD_QR`` 值为1

### 6. 懒人微信群
![wechat](http://wx1.sinaimg.cn/large/800facaagy1g67r5irl91j217y0u0tem.jpg)
