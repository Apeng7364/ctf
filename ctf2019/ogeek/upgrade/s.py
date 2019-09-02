# -*- coding: utf-8 -*-
import os
import random
import string
from flask import Flask, request, session
from flask_uploads import UploadSet, configure_uploads, patch_request_class, ALL
from hashcash import check
from base64 import b64encode

app = Flask(__name__)
app.secret_key = "waiting_for_replace"
firmware = UploadSet('firmware', extensions=ALL,default_dest=lambda app:os.getcwd()+'/tmp_rom/')
configure_uploads(app, firmware)
patch_request_class(app,size=20*1024)

html = '''
    <!DOCTYPE html>
    <title>Upgrade</title>
    <h1>Firmware Upload</h1>
    <h4>please proof your work:hashcash -mb28 %s</h4>
    <form action='upload' method=post enctype=multipart/form-data>
         <p style='display:inline'>firmware:</p><input type=file name=firmware>
         <br>
         <p style='display:inline'>pow stamp:</p><input type=text name=pow>
         <br>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST' and 'firmware' in request.files:
        if 'r' not in session or 'pow' not in request.form or not check(request.form['pow'],bits=28,resource=session['r']):
            return '<h1>too lazy,buddy,too lazy</h1>'
        session.pop('r')
        filename = firmware.save(request.files['firmware'],name='rom.upg')
        print(filename)
        cmd = 'su upguser -c "/bin/upg '+os.getcwd()+'/tmp_rom/'+filename + ' ' +b64encode(os.urandom(8)) +'"'
        print(cmd)
        os.system(cmd)
        return '<h1>Upgrading, there won\'t be any notice when we are done</h1>'
    return '<h1>Something is missing</h1>'

@app.route('/',methods=['GET'])
def index():
    r = ''.join([string.ascii_letters[random.randint(0,25)] for i in range(8)])
    session['r'] = r
    return (html % r)



if __name__ == '__main__':
    #app.run(host="0.0.0.0",port=80,debug=True)
    app.run(debug=False)

