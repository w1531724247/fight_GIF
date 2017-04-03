from flask import Blueprint

square = Blueprint('square', __name__)
category = Blueprint('category', __name__)

import squareViews
import categoryViews
