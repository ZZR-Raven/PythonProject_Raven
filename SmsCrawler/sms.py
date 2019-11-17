import re
import json
import requests
from selenium import webdriver
from lxml import etree
from scrapy.selector import Selector
import scrapy
import lxml

# 创建环境
smsurl = 'http://www.scut.edu.cn/sms/'
driver = webdriver.Chrome()
driver.get(smsurl)
input('请手动输入账号密码')

# 拿到每个人的id号
id_code = driver.get('http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/evaluation/intellectualList.jsp')
id_source = driver.page_source
print(id_source)
id_list = []
id_list = re.findall('evaluationId=(.*?)&amp;classYearId=13',id_source,re.S)
print(id_list)

# 获取源代码
url1 = 'http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/module/evaluation/studentIntellectualDetail.jsp?evaluationId='
url2 = '&classYearId=13'
for id in id_list:
    url = url1 + id + url2
    info_code = driver.get(url)
    info_source = driver.page_source
    with open(id+'.txt','w',encoding='utf-8',errors = 'ignore') as info :
        info.write(info_source)


