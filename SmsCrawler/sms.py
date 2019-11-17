import re
import json
import requests
from selenium import webdriver
from lxml import etree
from scrapy.selector import Selector
import scrapy
import lxml


smsurl = 'http://www.scut.edu.cn/sms/'
driver = webdriver.Chrome()
driver.get(smsurl)
input('请手动输入账号密码')

id_code = driver.get('http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/evaluation/intellectualList.jsp')
id_source = driver.page_source
print(type(id_code))
id_list = []
id_list = re.findall('evaluationId=(.*?)&amp;classYearId=13',id_source,re.S)
print(id_list)
# id_list = ['4461', '2911', '10233', '10245', '10246', '10249', '10254', '10257', '7490', '10283', '10285', '10298', '10300', '10303', '10305', '10307', '10334', '10337', '10343', '10348', '10362', '10369', '949', '10379', '10392', '6552', '10400', '10407', '4841', '1319', '10431', '3422', '10450', '1024', '6577', '3375', '10475', '10478', '10723', '6563', '4850', '10893', '10900']

# testurl = 
# '''
# http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/module/evaluation/studentIntellectualDetail.jsp?evaluationId=4461&classYearId=13
# '''
# test_code = driver.get('http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/module/evaluation/studentIntellectualDetail.jsp?evaluationId=4461&classYearId=13')#.content.decode(encoding = 'utf-8',errors = 'ignore')
# test_source = driver.page_source
# print(test_source)


url1 = 'http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/module/evaluation/studentIntellectualDetail.jsp?evaluationId='
url2 = '&classYearId=13'
for id in id_list:
    url = url1 + id + url2
    info_code = driver.get(url)
    info_source = driver.page_source
    with open(id+'.txt','w',encoding='utf-8',errors = 'ignore') as info :
        info.write(info_source)



# real_url = []
# # with open('zhiyu.html',encoding='utf-8') as handcv:
# #     hhh = handcv.read()
# url_list = re.findall('<td><a href="(.*?)" target=',str(hhh))
# for url in url_list:
#     real_url.append('http://xsgl.7i5q.cas.scut.edu.cn' + url)  
# scorelist = re.findall('<td>(\\d.\\d)</td>',str(hhh))
# print(scorelist)
# finallist = []
# i = 0
# for score in scorelist:
#     if i%2 == 0:
#         finallist.append(scorelist[i]) 
#     i = i + 1
# print(finallist)

