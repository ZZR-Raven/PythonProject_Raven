import scrapy
import lxml
import requests
import redis
import chardet
from lxml import etree
from scrapy.selector import Selector


# #   user check  ##########################    
# ch_name = '龙族前传'
# ch_xpath = '/html/body/div[@align="center"]/table/tr/td/p/text()'
# ch_url = 'https://www.kanunu8.com/book3/7750/'
# #   user check  ##########################    

#   user check  ##########################    
ch_name = '龙族前传'
ch_xpath = '/html/body/div[@align="center"]/table/tr/td/p/text()'
ch_url = 'https://www.kanunu8.com/book3/7750/'
#   user check  ##########################   

#   连接redis
pool = redis.ConnectionPool() 
client = redis.Redis(connection_pool=pool)
#   先清空目标txt文件防止被重复写入
with open(ch_name+'.txt','w',encoding='utf-8') as temp:  
    temp.truncate()

def url_list_Byte2Str():
    url_b = client.rpop('url_list')
    url_s = str(url_b,encoding='utf-8')
    return url_s
    # ch_byte = requests.get(url_s).content
    # charset_dict = chardet.detect(ch_byte)
    # charset = charset_dict['encoding']

def get_charset(byte_code):
    charset_dict = chardet.detect(byte_code)
    return charset_dict['encoding']

ch_count = 0
def TextGet_OneTXT():
    print('start!')
    global ch_count     #函数内引用全局变量要加global关键字
    ch_count = ch_count + 1
    url = url_list_Byte2Str()
    ch_byte = requests.get(url).content
    charset = get_charset(ch_byte)
    ch_code = ch_byte.decode(encoding = charset,errors = 'ignore')
    selector = etree.HTML(ch_code)
    # 要从源码看，chrome直接复制xpath可能有多余的误导标签
    ch_pre = selector.xpath(ch_xpath)
    with open(ch_name + '.txt','a',encoding='utf-8') as t1:  
        t1.writelines(ch_pre)


def Check_RedisList():
    #确保名为url_list的redis list不存在
    if client.exists('url_list') == True:
        client.delete('url_list')
        print('the key has been deleted')
    else:
        print('the key isn\'t exists')

    

def Get_ChUrl():
    #   爬取小说每章节url
    ori_code = requests.get(ch_url).content.decode(encoding = 'gb2312')
    selector = etree.HTML(ori_code)
    url_list = selector.xpath('//tbody/tr/td/a/@href')
    url_list.pop(0)     #去掉第一个无用网址
    #   将url补充成html路径并放入redis的list中
    for url in url_list:
        real_url = ch_url+url
        client.lpush('url_list',real_url)    



if __name__ == '__main__':
    Check_RedisList()
    Get_ChUrl()
    while client.exists('url_list') == True:
        TextGet_OneTXT()
    print('all done!')



