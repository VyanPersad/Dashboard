from flask import request
from datetime import datetime as dt
import os
def date_File():
    year = dt.now().year
    day = dt.now().day 
    month = dt.strftime(dt.now(),'%B')
    return [year, day, month]