from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__)

text = "AWA"

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
            return {"code": "200", "msg": "上传成功"}
        else:
            return {"code": "200", "msg": "token错误"}

@app.route('/gettext')
def gettext():
    global text
    return text


app.run(host='0.0.0.0', port=81)
