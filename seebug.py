#coding:utf-8

import requests
import re
from selenium import webdriver
import csv
import datetime
import time
from lxml import etree



def getMaxNumber():

    url="https://www.seebug.org/vuldb/vulnerabilities"
    global time
    global title_str
    global re_title
    global title_str
    chrome = webdriver.Chrome()
    chrome.get(url)
    #time.sleep(5)


    __jsluid = '__jsluid=' + chrome.get_cookie('__jsluid')['value'] + ';'
    __jsl_clearance = '__jsl_clearance=' + chrome.get_cookie('__jsl_clearance')['value'] + ';'
    chrome.quit()

    headers={
        "Host": "www.seebug.org",
        "Connection": "close",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://www.seebug.org/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": __jsluid + __jsl_clearance
            }

    requests.packages.urllib3.disable_warnings() 
    res=requests.get(url,headers=headers,verify=False).text
    html=etree.HTML(res)

    title=html.xpath('/html/body/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]/a/text()')
    title_str="".join(title)
    t=int(title_str[4:])
    return t



def doSth(url):
    global time
    global re_title
    global title_str
    chrome = webdriver.Chrome()
    chrome.get(url)
    #time.sleep(5)


    __jsluid = '__jsluid=' + chrome.get_cookie('__jsluid')['value'] + ';'
    __jsl_clearance = '__jsl_clearance=' + chrome.get_cookie('__jsl_clearance')['value'] + ';'
    #csrftoken='csrftoken='+ chrome.get_cookie('csrftoken')['value']+';'

    chrome.quit()

    headers={
        "Host": "www.seebug.org",
        "Connection": "close",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://www.seebug.org/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": __jsluid + __jsl_clearance #+ csrftoken
            }

    requests.packages.urllib3.disable_warnings() 
    res=requests.get(url,headers=headers,verify=False).text
    html=etree.HTML(res)



    title=html.xpath('//*[@id="j-vul-title"]/span/text()')
    title_str="".join(title)
    time=html.xpath('//*[@id="j-vul-basic-info"]/div/div[1]/dl[2]/dd/text()')
    time_str="".join(time)
    number=html.xpath('//*[@id="j-vul-basic-info"]/div/div[3]/dl[1]/dd/a/text()')
    number_str="".join(number)
    step=html.xpath('//*[@id="j-vul-basic-info"]/div/div[1]/dl[4]/dd/div[1]/@data-original-title')
    step_str="".join(step)
    desc=html.xpath('//*[@id="j-affix-target"]/div[2]/div[1]/section[2]/div[2]/div[2]/p[1]/text()')
    desc_str="".join(desc)
    articles.append([title_str,time_str,number_str,step_str,desc_str])
    
    headers=["标题","时间","编号","危害级别","漏洞描述"]

  
                #保存在csv文件中
    with open("seebug.csv","a",newline="") as f:
        writer=csv.writer(f,dialect=("excel"))
        writer.writerow(headers)
        for row in articles:
            writer.writerow(row)
 


    
articles=[]
a=getMaxNumber()
url="https://www.seebug.org/vuldb/ssvid-"
for i in range(a-5,a-2):
    a=str(i)
    f=open("title.txt")
    source=f.read()
    if a in source:
        continue
    else:
        url_data=url+a
        doSth(url_data)
        articles=[]
        with open("title.txt",'a') as f:
            f.write(a)
            f.write('\n')
            f.close()

'''def main(h=1,m=0):  
    while True:  
        now = datetime.datetime.now()  
        # print(now.hour, now.minute)  
        if now.hour == h and now.minute == m:  
            break  
        # 每隔60秒检测一次   
        time.sleep(60)  
    doSth()#爬虫程序
'''
