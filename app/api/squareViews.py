#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, flash, redirect, url_for, jsonify, json
from . import square
from .. import db

@square.route('/', methods=['GET'])
def helloSquare():
    return 'helloSquare'