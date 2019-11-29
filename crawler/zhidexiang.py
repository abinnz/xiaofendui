# -*- coding: utf-8 -*-
import logging
import crawler
from crawler.post import PostDetail

# 值得享列表地址
BASE_LIST_URL = 'http://ym.jiucaiqq.com:8060/api/post/list'
# 值得享详细页地址
BASE_DETAIL_URL = 'http://ym.jiucaiqq.com:8060/post/%s'


'''
值得享爬虫
'''
class ZhiDeXiangCrawler(object):

    def __init__(self):
        pass

    def crawl(self):
        post_list = []
        logging.info('Crawl url: ' + BASE_LIST_URL)
        result = crawler.get_resp_json(BASE_LIST_URL)
        if result['code'] != 'success':
            logging.info('Crawl error: %s!' % result['msg'])
            return post_list
        for item in result['data']['list']:
            post_detail = PostDetail()
            post_detail.id = str(item['id'])
            post_detail.title = item['title']
            post_detail.time = item['createTime']
            post_detail.url = BASE_DETAIL_URL % item['id']
            post_detail.images = item['images']
            post_detail.mall = item['mall']
            post_detail.content = item['content']
            post_detail.resource = item['resource']
            if 'smzdm' == item['resource']:
                post_detail.source = item['resourceTag']
            elif 'weibo' == item['resource']:
                post_detail.source = item['userName']
            else:
                post_detail.source = item['resource']
            post_detail.permission = item['permission']
            post_detail.name = item['userName']
            post_list.append(post_detail)
        return post_list
        