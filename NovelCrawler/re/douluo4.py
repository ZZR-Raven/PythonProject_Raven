import os
import re
import time
import requests
# from multiprocess.dummy import Pool

title_code = requests.post('http://www.yunxs.com/canglanjue/').content.decode()
# with open('title_post.txt','w',encoding='utf-8') as txt1:
#    txt1.write(title_code)

#   先清空目标txt文件防止被重复写入
with open('终极斗罗.txt','w',encoding='utf-8') as temp:  #
    temp.truncate()

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

#如果没有文件夹就建一个,如果有就不建
# os.makedirs('终极斗罗',exist_ok=True)

num = 0
while (num <= len(real_url)):
    print("request start")
    code_html = requests.get(real_url[num])
    code_bytes = code_html.content
    print("decode start")
    code_str = code_bytes.decode("UTF-8","ignore")
    # ch = ch_name[num]
    ar = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',code_str,re.S)
    with open('终极斗罗.txt','a',encoding='utf-8') as txt2:  
        txt2.writelines(ar) 
    print('第%d章打印完成'%num)
    num = num + 1





