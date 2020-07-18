import requests
from lxml import etree
import re

url = "https://leetcode-cn.com/problemset/all/"
headers = {
    'Host': 'leetcode-cn.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://leetcode-cn.com/',
    'Upgrade-Insecure-Requests': "1",
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers'
}


def getlabel_dic():
    response = requests.get(url=url, headers=headers)
    response.encoding = "utf-8"
    html = etree.HTML(response.text)
    label_name_list_temp = html.xpath('//a[@class="btn btn-xs btn-default round-btn tags-btn sm-topic"]/span[1]/text()')
    label_name_list = []
    for label_name in label_name_list_temp:
        result = re.findall(u"[\u4e00-\u9fa5a-zA-Z0-9]+", label_name)
        if len(result) == 1:
            label_name_list.append(result[0])
        elif len(result) == 2:
            label_name_list.append(result[0] + " " + result[1])
        elif len(result) == 3:
            label_name_list.append(result[0] + " " + result[1] + " " + result[2])
    label_url_list_temp = html.xpath('//a[@class="btn btn-xs btn-default round-btn tags-btn sm-topic"]/@href')
    label_url_list = []
    for label_url in label_url_list_temp:
        label_url = str(label_url).split('/')[2]
        label_url_list.append(label_url)
    label_dic = {}
    for i in range(len(label_url_list)):
        label_dic[label_name_list[i]] = label_url_list[i]
    return label_dic
