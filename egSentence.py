# This file is for example sentence
#!python3

#import lib
from selenium import webdriver
import urllib.request, urllib.parse, urllib.error
import re
import ssl
from bs4 import BeautifulSoup
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


# use firefox as sebrowser
driver = webdriver.Firefox()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# enter url
# url = input('Enter url: ')
url = 'https://ko.dict.naver.com/#/search?query='

# open data file
# fn = input('Enter file name: ')
# fh = open(fn)
fh = open('so.txt')

# open save file
#sfn = input('Enter file name: ')
fout = open('test0.txt' ,'a', encoding='utf-8') # write in file for note



for vocab in fh:
    vocab = vocab.rstrip() # split the line
    trueurl = url + vocab  # send query

    driver.get(trueurl)
    time.sleep(1)
    html = driver.page_source
#    time.sleep(5)
    soup = BeautifulSoup(html, 'html.parser')
#    contents = soup.find_all("div", class_='row')


    try:
        contents = soup.find_all("p", class_='text') # add def of vocab
        uni = contents[0].get_text()
        fout.write(uni + '\n')

    except:
        fout.write(vocab+'NOT FOUND\n')
