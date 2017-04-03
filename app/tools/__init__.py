from flask import Blueprint
from crawler import Crawler
emojiCrawler = Crawler()
tools = Blueprint('tools', __name__)

import views

