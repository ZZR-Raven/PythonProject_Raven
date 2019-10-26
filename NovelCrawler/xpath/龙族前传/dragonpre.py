import scrapy
import lxml
import requests
import redis
import chardet
from lxml import etree
from scrapy.selector import Selector
import time
import re
from tqdm import tqdm

class xpath_crawler(object):

    bookname = '龙族前传'
    url_xpath = '//tbody/tr/td/a/@href'
    ch_xpath = '/html/body/div[@align="center"]/table/tr/td/p/text()'
    ch_url = 'https://www.kanunu8.com/book3/7750/'

    def __init__(self):
        self.pool = redis.ConnectionPool() 
        self.client = redis.Redis(connection_pool=self.pool)
        tqdm(ascii=True)

    # def connect_redis(self):
        # self.pool = redis.ConnectionPool() 
        # self.client = redis.Redis(connection_pool=self.pool)

    def cleardoc(self):
        with open(self.bookname+'.txt','w',encoding='utf-8') as temp:  
            temp.truncate()

    def url_list_Byte2Str(self):
        url_b = self.client.rpop('url_list')
        url_s = str(url_b,encoding='utf-8')
        return url_s

    def get_charset(self,byte_code):
        self.charset_dict = chardet.detect(byte_code)
        return self.charset_dict['encoding']

    ch_count = 0
    def TextGet_OneTXT(self):
        self.ch_count = self.ch_count + 1
        # print('start ch%s!'%(self.ch_count))
        url = self.url_list_Byte2Str()
        ch_byte = requests.get(url).content
        charset = self.get_charset(ch_byte)
        ch_code = ch_byte.decode(encoding = charset,errors = 'ignore')
        selector = etree.HTML(ch_code)
        # 要从源码看，chrome直接复制xpath可能有多余的误导标签
        self.ch_pre = selector.xpath(self.ch_xpath)
        outfp = open(self.bookname + '.txt', "a", encoding='utf-8') # 生成没有空行的文件
        #用于解决xpath带\r\n\t一堆空行的问题
        try:
            lines = list(self.ch_pre)
            for li in lines:
                if li.split():
                    outfp.writelines(li)
        finally :
            outfp.close()

    def Check_RedisList(self):
        #确保名为url_list的redis list不存在
        if self.client.exists('url_list') == True:
            self.client.delete('url_list')
            print('the key has been deleted')
        else:
            print('the key isn\'t exists')

    def get_len(self):
        if self.client.exists('url_list') == True:
            self.listlen = self.client.llen('url_list')


    def user_call(self):
        self.Check_RedisList()
        self.cleardoc()
        self.Get_ChUrl()
        # while self.client.exists('url_list') == True:
            # self.TextGet_OneTXT()
        self.get_len()
        # with tqdm(range(self.listlen)) as self.pbar:
            # self.pbar.close()
        for self.ch in tqdm(range(self.listlen)):
            self.TextGet_OneTXT()
            # self.pbar.update(1)
        print('all done!')

    def Get_ChUrl(self):
        #   爬取小说每章节url
        self.ori_code = requests.get(self.ch_url).content.decode(encoding = 'gb2312',errors = 'ignore')
        # with open('code.html','w',encoding='utf-8') as test:  
        #     test.write(self.ori_code)
        self.selector = etree.HTML(self.ori_code)
        self.url_list = self.selector.xpath(self.url_xpath)
        self.url_list.pop(0)     #去掉第一个无用网址
        #   将url补充成html路径并放入redis的list中
        for url in self.url_list:
            real_url = self.ch_url+url
            self.client.lpush('url_list',real_url)    
            


if __name__ == '__main__':
    xpath_user = xpath_crawler()
    time_start = time.time()
    xpath_user.user_call()
    time_used = time.time() - time_start
    print('本次爬取共用时%ds'%time_used,'，共%d章'%(xpath_user.ch_count))
    av_time = time_used/(xpath_user.ch_count)
    print('平均每章用时%fs'%av_time)

# 本次爬取共用时12s ，共11章
# 平均每章用时1.163830s