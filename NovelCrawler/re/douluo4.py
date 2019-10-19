import os
import re
import time
import requests
# from multiprocess.dummy import Pool

title_code = requests.post('http://www.yunxs.com/canglanjue/').content.decode()
with open('title_post.txt','w',encoding='utf-8') as txt1:
   txt1.write(title_code)

real_url = []
# '/html/body/div[10]/div[1]/div[2]/ul/li[1]'
ch_url = re.findall('/html/body/div[10]/div[1]/div[2]/a href="(.*?)">',str(title_code),re.S)
#print(ch_url)      这里是每章的url
# ch_name = re.findall('.html">(.*?)</a></dd><dd><a',str(title_code),re.S)
#print(ch_name)     这里是每章的名字
for url_test in ch_url:
    real_url.append('https://www.kanunu8.com/book2/10943/' + str(url_test))  #每章网址




