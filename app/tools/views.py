#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, jsonify, json
from . import tools, emojiCrawler
from .. import db
from ..models import Emoji


@tools.route('/addDTBQ', methods=['GET'])
def addDTBQ():
    for page in range(1,35):#1-34页
        print page
        htmlString = emojiCrawler.qqtnWithPageID(page_id=str(page))
        emojis = emojiCrawler.extractEmojiValues(htmlString=htmlString)
        for value in emojis:
            title = value['title']
            imgSrc = value['imgSrc']
            likes = value['likes']
            creatTime = value['creatTime']
            emoji = Emoji(title=title,imgSrc=imgSrc,likes=likes,creatTime=creatTime)
            db.session.add(emoji)
        db.session.commit()

    return "add success!"