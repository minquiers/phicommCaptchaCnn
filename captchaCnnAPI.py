# coding:utf-8
# !flask/bin/python
import util
from flask import Flask, jsonify, request
from  captcha_cnn import  image2text

app = Flask(__name__)


@app.route('/vcode', methods=['POST'])
def get_tasks():
    if not request.json or not 'base64' in request.json:
        return '1000'
    if not request.json or not 'token' in request.json:
        return '2000'
    if request.json.get('token') != '1234567890123':
        return '2001'
    image = util.base64CoverImage(request.json.get('base64', ""))
    vcode =  image2text(image)
    print(vcode)
    return ''.join(vcode)


if __name__ == '__main__':
    app.run(debug=False)
