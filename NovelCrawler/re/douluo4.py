import os
import re
import time
import requests
# from multiprocess.dummy import Pool

# title_code = requests.post('http://www.yunxs.com/canglanjue/').content.decode()

# #   先清空目标txt文件防止被重复写入
# with open('终极斗罗.txt','w',encoding='utf-8') as temp:  #
#     temp.truncate()

real_url = []
# ch_url = re.findall('<a href="(.*?)">第',str(title_code),re.S)
# ch_url.pop(0)
# ch_url.pop(0)
# ch_url.pop(0)
# print(ch_url)      #这里是每章的url
# for url_test in ch_url:
#     real_url.append('http://www.yunxs.com/canglanjue/' + str(url_test))  #每章网址

# num = 0
# while (num <= len(real_url)):
#     print("request start")
#     code_html = requests.get(real_url[num])
#     code_bytes = code_html.content
#     print("decode start")
#     code_str = code_bytes.decode("UTF-8","ignore")
#     ar = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',code_str,re.S)
#     with open('终极斗罗.txt','a',encoding='utf-8') as txt2:  
#         txt2.writelines(ar) 
#     print('第%d章打印完成'%num)
#     num = num + 1

class re_crawler(object):

    bookname = '终极斗罗'
    list_url = 'http://www.yunxs.com/canglanjue/'
    list_re = '<a href="(.*?)">第'
    real_url = []

    def __init__(self):
        pass

    def clearDoc(self):
        # 先清空目标txt文件防止被重复写入
        with open(self.bookname + '.txt','w',encoding='utf-8') as temp:  #
            temp.truncate()

    def get_url_list(self):
        self.title_code = requests.post(self.list_url).content.decode()
        self.ch_url = re.findall(self.list_re,str(self.title_code),re.S)
        self.ch_url.pop(0)
        self.ch_url.pop(0)
        for url_test in self.ch_url:
            self.real_url.append('http://www.yunxs.com/canglanjue/' + str(url_test))  #每章网址

    def get_article(self):
        self.num = 0
        while (self.num < len(real_url)):
            print("ch%d request start"%self.num)
            code_html = requests.get(real_url[self.num])
            code_bytes = code_html.content
            code_str = code_bytes.decode("UTF-8","ignore")
            ar = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',code_str,re.S)
            with open('终极斗罗.txt','a',encoding='utf-8') as txt2:  
                txt2.writelines(ar) 
            print('第%d章打印完成'%self.num)
            self.num = self.num + 1
    
    def user_call(self):
        self.clearDoc()
        self.get_url_list()
        self.get_article()



if __name__ == '__main__':
    re_user = re_crawler()
    re_user.user_call()
