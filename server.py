# coding: utf-8

import flask
from line_api import LineApi

app = flask.Flask(__name__)
api = LineApi()

@app.route('/')
def index():
    return 'Hello, Line API'

@app.route('/webhook', methods=['POST'])
def webhook():
    msgs = flask.request.json['events']
    for msg in msgs:
        text = msg['message']['text']
        api.message_reply(msg['replyToken'], "reply: " + text)
        print msg['source']['userId']
    
    return ''

@app.route('/message/push/<userid>/<text>')
def message_push(userid, text):
    api.message_push(userid, "push: " + text)
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080, debug=True)
