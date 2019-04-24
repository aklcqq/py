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

# prettify meaning
def cn_meaning(raw_meaning):
    split_meaning = raw_meaning.split('>')
    cn_meaning = split_meaning[1]
    split_meaning = cn_meaning.split('<')
    return split_meaning[0]

# convert to utf8
def utf_hangul(vocab):
    vocab = vocab.rstrip()
    ###vocab to utf-8
    vocab = vocab.encode()
    vocab = str(vocab)
    vocab = str.upper(vocab)
    vocab = vocab[2:]
    vocab = vocab.replace('\\X','%')
    vocaba = vocab.split("'")
    vocab = vocaba[0]
    return vocab

def get_id(vocab):
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

"""
fn = input('Enter file name: ')
fh = open(fn)
"""
## preparation for url
vocab = input('E:')
src_word = vocab
vocab = utf_hangul(vocab)
## create url
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
print(word_id)

fur_url = 'https://zh.dict.naver.com/#/entry/kozh/' + word_id

# use firefox as sebrowser
driver = webdriver.Firefox()

driver.get(fur_url)
time.sleep(1)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

hanjas = soup.find_all("p", class_='entry_mean') # add hanja
print(hanjas[0].get_text())
