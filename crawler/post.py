# -*- coding: utf-8 -*-
import re
import json
import os
import crawler
from PIL import Image
from io import BytesIO
from time import time


'''
帖子详细内容
'''
class PostDetail(object):
    def __init__(self, url=''):
        self.id = ''
        self.title = ''
        self.url = url
        self.time = ''
        self.source = ''
        self.resource = ''
        self.permission = 0
        self.content = ''
        self.name = ''
        self.images = []
        self.tags = []
        self.mall = ''

    def format_msg(self, enable_url=False, enable_source=False):
        if self.title == '':
            content = '%s\n' % (self.content)
        else:
            content = '%s\n\n%s\n' % (self.title, self.content)
        if self.permission != 0:
            content = '【权%s】%s' % (self.permission, content)
        content += '\n'
        if enable_url:
            content += '手机端：%s\n' % (self.url)
        if not enable_source:
            return content
        content += '【来源：%s】' % (self.resource)
        if self.resource == 'weibo':
            content += '【%s】' % (self.name)
        elif self.resource == 'smzdm':
            content += '【%s】' % (self.source)
        return content

    # 合并图片
    def merge_image(self, save_path='/tmp'):
        if len(self.images) == 0:
            raise Exception('当前内容图片数量为零!')
        images = []
        max_width = 0
        max_height = 0
        for image in self.images:
            image = Image.open(BytesIO(crawler.get_resp(image).content))
            # 获取图片最大宽度
            if max_width < image.size[0]:
                max_width = image.size[0]
            images.append(image)
        # 等比例缩放图片
        for index, image in enumerate(images):
            images[index] = image.resize((max_width, int(max_width / image.size[0] * image.size[1])))
            max_height += images[index].size[1]
        merge_image = Image.new('RGB', (max_width, max_height), 'white')
        # 拼接图片
        height = 0
        for image in images:
            merge_image.paste(image, (0, height))
            height += image.size[1]
        path = os.path.join(save_path, str(int(time() * 1000)) + '.jpg')
        merge_image.save(path)
        return path
    
    # 下载图片
    def download_image(self, save_path='/tmp'):
        paths = []
        for url in self.images:
            path = os.path.join(save_path, os.path.basename(url))
            f = open(path, 'wb')
            f.write(crawler.get_resp(url).content)
            f.close()
            paths.append(path)
        return paths

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)
        