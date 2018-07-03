# -*- coding: utf8 -*-
from  flask import Flask,request,jsonify,make_response,abort

from flask_restful import reqparse

app=Flask(__name__)

import datetime

import time




@app.route('/', methods=[ 'POST'])
def remotePc():
    return
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'msg':'fail','error': '404 Not found'}), 404)

@app.errorhandler(500)
def not_found(error):
    return make_response("程序报错，可能是因为叙利亚战争导致", 500)
if __name__=="__main__":

    # print('performance_not_ok1:',performance_not_ok)
    app.run(host='127.0.0.1',debug=True,threaded=True,port=5202)