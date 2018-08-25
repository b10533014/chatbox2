# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('78Hiir+TqQ+JVys6dK/AGnC+qGdF3K3RWsu72jXoeweizrQmuntZYgx64CYRWbabWnd98mk4ZgiSsWbnTt3Uq0LtlP3LxY96DUTea8V4terYrruPQRp0vyY/5tAnkMSjArHsp11UAXPwxQWy4Cgs+QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('U071f9173959eeb8b8359adcc23b916f8')



@app.route("/callback", methods=['POST'])
def callback():

    
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)