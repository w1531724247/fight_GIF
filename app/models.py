#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import db

class Emoji(db.Model):
    __tablename__ = 'emoji'
    id = db.Column(db.Integer, primary_key=True)
    imgSrc = db.Column(db.String)#图片地址
    title = db.Column(db.String)#标题
    descript = db.Column(db.String)#描述
    likes = db.Column(db.String)#点赞
    creatTime = db.Column(db.String)#创建时间

    def __init__(self, imgSrc="", title="", descript="",likes="",creatTime=""):
        self.imgSrc = imgSrc
        self.title = title
        self.descript = descript
        self.likes = likes
        self.creatTime = creatTime
        return