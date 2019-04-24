#!python3
import urllib.request, urllib.parse, urllib.error
import ssl
import re
import json
import time

from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

## def

# convert to utf8
def get_id(vocab):
    vocab = vocab.rstrip()
    ###vocab to utf-8
    vocab = vocab.encode()
    vocab = str(vocab)
    vocab = str.upper(vocab)
    vocab = vocab[2:]
    vocab = vocab.replace('\\X','%')
    vocaba = vocab.split("'")
    vocab = vocaba[0]

    rawurl = 'https://zh.dict.naver.com/api3/zhko/tooltip?query='
    url = rawurl + vocab

    uhp = urllib.request.Request(url, headers=hdr)
    uh = urllib.request.urlopen(uhp, context=ctx)
    data = uh.read().decode()
    data = data.rstrip()
    datajs = json.loads(data)

    jsre = datajs['jsonResult']
    datajsre = jsre[0]
    word_id = datajsre['entryId']
    return word_id


## ignore ssl certificate error

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

hdr = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

fn = input('Enter file name: ')
fh = open(fn)
word_id_list = list()
for vocab in fh:
    try:
        word_id = get_id(vocab)
        word_id_list.append(word_id)
    except:
        print('NOT FOUND:'+ vocab)

for id in word_id_list:
    print(id)


# use firefox as sebrowser
driver = webdriver.Firefox()

for id in word_id_list:
    ## preparation for url
    word_id = id
    fur_url = 'https://zh.dict.naver.com/#/entry/kozh/' + word_id

    driver.get(fur_url)
    time.sleep(1)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    word_mean = soup.find_all("p", class_='entry_mean') # add meaning
    print(word_mean[0].get_text())
