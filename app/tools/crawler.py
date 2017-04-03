#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib, urllib2
import chardet
import re, os, sys
from lxml import etree


class Crawler():
    def cheWaWaCarSeriseList(self, brandid=''):
        #POST请求
        url = 'http://api.chewawa.com.cn/myapi/Insure_getCarSeriesList'
        params = {'brandid':brandid}
        params_urlencode = urllib.urlencode(params)
        req = urllib2.Request(url=url, data=params_urlencode)

        res_data = urllib2.urlopen(req)
        res = res_data.read()

        return res

    def qqtnWithPageID(self, page_id=''):
        #GET请求
        url = 'http://www.qqtn.com/bq/dtbq_' + page_id + '.html'
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
        res = res_data.read()
        chardit1 = chardet.detect(res)
        # htmlString = res.decode(chardit1['encoding']).encode('utf-8')
        htmlString = res.decode('gbk').encode('utf-8')

        return htmlString

    #获取所有的emoji元素通过正则表达式
    def extractEmojiElementWithRe(self, htmlString=''):
        pattern = re.compile(r'<a href="[a-z|0-9|/|.|_]*?" target="_blank" title=".*?" class="g-piclist-cont g-bqlist-cont">\s*?<p><span></span><img src=".*?" /></p>\s*?<strong>.*?</strong>\s*?<b><i></i>\d*?</b><em><i></i>[0-9|-]*?</em>\s*?</a>', re.S)
        items = re.findall(pattern, htmlString)

        return items

    #获取所有的emoji元素通过lxml
    def extractEmojiValues(self, htmlString):
        doc = etree.HTML(htmlString)
        all_div = doc.xpath('//div[@class="g-gxlist-box"]')#获取所有class="g-gxlist-box"的div标签
        targetDiv = all_div[1]
        all_a_item = targetDiv.xpath('.//a[@class="g-piclist-cont g-bqlist-cont"]')  #获取所有class="g-piclist-cont g-bqlist-cont"的a标签
        data = []
        for a in all_a_item:
            values = {}
            values['imgSrc'] = a.xpath('.//img/@src')[0]
            values['title'] = a.xpath('.//strong/text()')[0]
            values['likes'] = a.xpath('.//b/text()')[0]
            values['creatTime'] = a.xpath('.//em/text()')[0]
            data.append(values)

        return data

    #下载文件
    def downloadFileWithURL(self, fileUrl=''):
        fileName = urllib.unquote(fileUrl).decode('utf8').split('/')[-1]
        dirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fileName = dirPath + '/static/qqtn/' + fileName
        urllib.urlretrieve(fileUrl, fileName)
        pass