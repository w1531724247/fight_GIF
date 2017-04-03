#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, jsonify, json
from . import category
from .. import db

@category.route('/', methods=['GET'])
def helloCategory():
    return 'helloCategory'