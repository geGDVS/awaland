from flask import Flask
from flask import render_template
from flask import request
import os
import json
import boto3
s3 = boto3.client('s3')
  
app = Flask(__name__)

@app.route('/')
def index():
    return 'AWA!'

@app.route('/awaya', methods=['GET', 'POST'])
def uptext():
    global text
    if request.method != "POST":
        return render_template('index.html')
    else:
        if request.form["token"] == os.getenv("TOKEN"):
            text = request.form['text']
            # store something
            s3.put_object(
                Body=json.dumps({'text': text}),
                Bucket="cyclic-shy-tam-elk-us-west-1",
                Key="some_files/my_file.json"
            ) 
            return {"code": "200", "msg": "上传成功"}
        else:
            return {"code": "200", "msg": "token错误"}

@app.route('/gettext')
def gettext():
    # get it back
    my_file = s3.get_object(
        Bucket="cyclic-shy-tam-elk-us-west-1",
        Key="some_files/my_file.json"
    )
    text = json.loads(my_file['Body'].read())['text']
    return text

