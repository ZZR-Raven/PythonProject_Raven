import re
import json
import requests
from selenium import webdriver
from lxml import etree
from scrapy.selector import Selector
import scrapy
import lxml


class driver_crawler(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def driverget(self,url):
        self.driver.get(url)

    def driver_pause(self,*args):
        if len(args) == 0 :
            input('pause')
        else :
            for values in args:
                input(str(values)) 

if __name__ == '__main__':
    url_1 = 'http://www.scut.edu.cn/sms/'
    url_2 = 'http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/evaluation/intellectualList.jsp'
    id_re = 'evaluationId=(.*?)&amp;classYearId=13'

    url3_1 = 'http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/module/evaluation/studentIntellectualDetail.jsp?evaluationId='
    url3_2 = '&classYearId=13'

    user_driver = driver_crawler()
    user_driver.driverget(url_1)  
    user_driver.driver_pause('手动输入账号密码')
    user_driver.driverget(url_2)
    id_source = user_driver.driver.page_source
    id_list = []
    id_list = re.findall(id_re,id_source,re.S)
    for id in id_list:
        url = url3_1 + id + url3_2
        info_code = user_driver.driver.get(url)
        info_source = user_driver.driver.page_source
        with open(id+'.txt','w',encoding='utf-8',errors = 'ignore') as info :
            info.write(info_source)
        




