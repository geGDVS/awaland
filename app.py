from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/awaya', methods=['GET', 'POST'])
def uptext():
    global text
    if request.method != "POST":
        return render_template('index.html')
    else:
        if request.form["token"] == os.getenv("TOKEN"):
            text = request.form['text']
            with open('static/text', 'w') as f:
                f.write(text)
                f.close()
            return {"code": "200", "msg": "上传成功"}
        else:
            return {"code": "200", "msg": "token错误"}

@app.route('/gettext')
def gettext():
    with open('static/text') as f:
        text = f.read()
        f.close()
    return text

