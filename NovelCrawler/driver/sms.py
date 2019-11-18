import re
import json
import requests
from selenium import webdriver
from lxml import etree
from scrapy.selector import Selector
import scrapy
import lxml


class driver_crawler(object):

    first_url = ""
    input_word = ""

    def __init__(self,first_url):
        self.driver = webdriver.Chrome()
        self.driver.get(first_url)

    def driver_pause(self,*args):
        if len(args) == 0 :
            input('pause')
        else :
            for values in args:
                input(str(values))            






