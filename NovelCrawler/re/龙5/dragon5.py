import os
import re
import time
import requests


class re_crawler(object):

    bookname = '龙族5悼亡者的归来'
    list_url = 'http://www.yunxs.com/longzu5/'
    list_re = '<li><a href="(.*?)">'
    real_url = []

    def __init__(self):
        pass

    def churl_fordragon5(self):
        while(self.ch_url[0] != '2465876.html' ):
            self.ch_url.pop(0)


    def clearDoc(self):
        # 先清空目标txt文件防止被重复写入
        with open(self.bookname + '.txt','w',encoding='utf-8') as temp:  #
            temp.truncate()

    def get_url_list(self):
        self.title_code = requests.post(self.list_url).content.decode()
        self.ch_url = re.findall(self.list_re,str(self.title_code),re.S)
        self.churl_fordragon5()
        # print(self.ch_url)
        for url_test in self.ch_url:
            self.real_url.append(self.list_url + str(url_test))  #每章网址

    def get_article(self):
        self.num = 0
        while (self.num < len(self.real_url)):
            print("ch%d request start"%self.num)
            code_html = requests.get(self.real_url[self.num])
            code_bytes = code_html.content
            code_str = code_bytes.decode("UTF-8","ignore")
            ar = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',code_str,re.S)
            with open(self.bookname + '.txt','a',encoding='utf-8') as txt2:  
                txt2.writelines(ar) 
            print('第%d章打印完成'%self.num)
            self.num = self.num + 1
    
    def user_call(self):
        self.clearDoc()
        self.get_url_list()
        self.get_article()
        # print(self.ch_url[0])



if __name__ == '__main__':
    re_user = re_crawler()
    time_start = time.time()
    re_user.user_call()
    time_used = time.time() - time_start
    print('本次爬取共用时%ds'%time_used,'，共%d章'%len(re_user.real_url))
    av_time = time_used/(len(re_user.real_url))
    print('平均每章用时%f'%av_time)
# 本次爬取共用时127s ，共220章
# 平均每章用时0.577298