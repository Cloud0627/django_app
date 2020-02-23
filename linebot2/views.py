from django.shortcuts import render
from django.http import HttpResponse
import json
#import os
from linebot import (
            LineBotApi, WebhookHandler
            )
from linebot.exceptions import (
            InvalidSignatureError
            )
from linebot.models import (
            MessageEvent, TextMessage, TextSendMessage, LocationSendMessage
            )


line_bot_api = LineBotApi('/+GNuZWOEBTcVkstUbLC4+J7uzRcrUAKBH0/VVew4Mm/H697QEey/NsfLdRzkXnAmcmdbrjlEsLHwCPMQyznCRWzA92H9KrtUtbJG4+EVeU7MnrRLpP4eNkWmzAXLb//chNcuVAhYafT6ClzywUipQdB04t89/1O/w1cDnyilFU=')

def index(request):
   if request.method == 'POST':
      # リクエスト取得
      request_json = json.loads(request.body.decode('utf-8'))
      # LineBot ログの出力
      print(json.dumps(request_json,indent=2))

      replyToken = request_json["events"][0]["replyToken"]
      txtMessage = request_json["events"][0]["message"]["text"]
      
      try:
          if txtMessage == "位置":
              line_bot_api.reply_message(replyToken,LocationSendMessage(type="location",title="my locatin",address="うんこ",latitude=35.65910807942215,longitude=139.70372892916203,quick_reply=True))
          else: 
              line_bot_api.reply_message(replyToken, TextSendMessage(text=txtMessage))      
      except InvalidSignatureError:
          print(InvalidSignatureError)

      return HttpResponse("OK")
   else:
      return HttpResponse("This is bot api(GET).")
