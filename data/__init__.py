import logging
import os, config, json

'''
获取临时文件结果数据
'''
def get_tmp_result():
    temp_file = os.path.join(config.BASE_TMP_DIR, 'tmp.json')
    result = set()
    if os.path.exists(temp_file):
        with open(temp_file, 'r', encoding=config.UTF8_ENCODING) as f:
            result = set(json.load(f)['list'])
    return result

'''
保存临时结果数据
'''
def save_tmp_result(result, last_result):
    temp_file = os.path.join(config.BASE_TMP_DIR, 'tmp.json')
    # 存储结果
    with open(temp_file, 'w', encoding=config.UTF8_ENCODING) as f:
        # 超过数量清空
        if len(last_result) > 1500:
            last_result = result
        else:
            last_result = last_result | result
        last_result = dict(list=list(last_result))
        json.dump(last_result, f)
