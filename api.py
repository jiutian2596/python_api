# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:51:43 2020

@author: 28446
"""

import flask as f
import os
import sys
import re
from flask_cors import CORS

app = f.Flask(__name__)


# 跨域访问
@app.after_request
def af_request(resp):
    resp = f.make_response(resp)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp


CORS(app, supports_credentials=True)

if 'static' not in os.listdir(app.root_path):
    os.system('mkdir static')


@app.route('/', methods=['POST'])
def code():
    res = {'safe': '', 'result': '', 'error': '', 'files': []}
    temp = sys.stdout
    i = f.request.args.get('id')
    if i not in os.listdir('static'):
        os.system('mkdir static\%s' % i)
    cod = f.request.form.get('code')
    if re.findall('cd|remove|rm -rf|ls|pwd|kill|mkdir|system', cod, re.I) != []:
        res['error'] = 'No permission!!!'
        res['safe'] = 'false'
        return res
    res['safe'] = 'true'
    try:
        with open('static/' + i + '/log.txt', 'w', encoding='utf-8') as log:
            sys.stdout = log
            exec(cod)
    except Exception as e:
        with open('static/' + i + '/log.txt', 'r', encoding='utf-8') as log:
            res['result'] = log.read()
        res['error'] = str(e)
    sys.stdout = temp
    os.remove('static/' + i + '/log.txt')
    if os.listdir('static/' + i) != []:
        for k in os.listdir('static/' + i):
            res['files'].append(f.url_for('static', filename=i + '/' + k))
    return f.jsonify(res)


@app.route('/upload', methods=['POST'])
def upload():  # 上传文件
    i = f.request.args.get('id')
    upload_file = f.request.files['touch']
    if upload_file:
        upload_file.save(os.path.join('static', i, upload_file.filename))
        return f.jsonify({'state': 'success'})
    else:
        return f.jsonify({'state': 'failed'})


@app.route('/delete')
def delete():  # 删除文件
    try:
        i = f.request.args.get('id')
        filena = f.request.args.get('file_name')
        os.remove('static/' + i + '/' + filena)
        return f.jsonify({'state': 'success'})
    except Exception:
        return f.jsonify({'state': 'error'})


app.run('192.168.1.240', port=5000)  # 服务器IP地址
