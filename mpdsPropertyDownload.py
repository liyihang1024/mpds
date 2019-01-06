#!/usr/bin/env python3
#coding:utf-8

'''
从晶体结构数据库MPDS的API批量下载晶体数据.
usage:通过修改search的内容控制搜索结果.
Author@LiYihang
<liyihang@shu.edu.cn>
'''

import urllib
from urllib.parse import urlencode
import httplib2
import json
import sys

api_key = "NP6d0ZuM0qKqDwd70p2sqlxfLiFp1IayPdRFRRMhdR37Ue28" # your key
endpoint = "https://api.mpds.io/v0/download/facet"
search = {
         "elements": "O",
         "classes": "spinel",
         #"sgs": "Pd-3m",
         "props": "entropy"
}

req = httplib2.Http()
response, content = req.request(
    uri=endpoint + '?' + urlencode({
        'q': json.dumps(search),
        'pagesize': 1000,
        'dtype': 1 ,# see query string parameters documentation
        # 'fmt' : 'cif'
    }),
    method='GET',
    headers={'Key': api_key}
)

if response.status != 200:
    # NB 400 means wrong input, 403 means authorization issue etc.
    # see https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    raise RuntimeError("Error code %s" % response.status)

#content = json.load(content)
file=open('propsData',mode='wb+')
file.write(content)
file.close()
