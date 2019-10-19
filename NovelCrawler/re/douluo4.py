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
'/html/body/div[@class=Layout no_h]/div[@class=Con jj_pl]/div[@class=list_box]/ul/li/'
ch_url = re.findall('<a href="(.*?)">第',str(title_code),re.S)
ch_url.pop(0)
ch_url.pop(0)
ch_url.pop(0)
print(ch_url)      #这里是每章的url
# ch_name = re.findall('.html">(.*?)</a></dd><dd><a',str(title_code),re.S)
#print(ch_name)     这里是每章的名字
for url_test in ch_url:
    real_url.append('http://www.yunxs.com/canglanjue/' + str(url_test))  #每章网址






