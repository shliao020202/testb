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

line_bot_api = LineBotApi('tfeKeC8lMV394uWm7M30OqW5sMW5P22ohFvEkNCxpNB+Tbcz1NRu7BWsdRyF4bOj0gJcMeNXJhzSOFL/nORzkc60Ybwj16uL9T/XqBX0jqeOMLnoXO1i1k+1S0eyDvAxXuGQydfhFXEYARAM7Vf85wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8e190269c4b1878f90bef815f7fad4df')



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