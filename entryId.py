import urllib.request, urllib.parse, urllib.error
import ssl
import re
import json

## def

def cn_meaning(raw_meaning):
    split_meaning = raw_meaning.split('>')
    cn_meaning = split_meaning[1]
    split_meaning = cn_meaning.split('<')
    return split_meaning[0]

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
