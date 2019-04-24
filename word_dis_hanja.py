# This file is for all
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
url = 'https://opendict.korean.go.kr/search/searchResult?focus_name=query&query='

# open data file
fn = input('Enter file name: ')
fh = open(fn)

# open save file
sfn = input('Save to file: ')
fout = open(sfn ,'a', encoding='utf-8') # write in file for note


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
        hanjas = soup.find_all("span", class_='search_word_sub') # add hanja
        hanja = hanjas[0].get_text() # get str
        hanja = hanja.replace('(','[')
        hanja = hanja.replace(')',']')

        contents = soup.find_all("span", class_='word_dis') # add def of vocab
        uni = contents[0].get_text()
        fout.write(vocab + hanja + ':'+ uni +'\n')

    except:
        fout.write(vocab+'NOT FOUND\n')
