from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
   if request.method == 'POST':
      # リクエスト取得
      request_json = json.loads(request.body.decode('utf-8'))
      # LineBot ログの出力
      print(json.dumps(request_json,indent=2))

      replyToken = request_json["events"][0]["replyToken"]

      return HttpResponse("This is bot api(POST).")
   else:
      return HttpResponse("This is bot api(GET).")

#返信はここにデータを送る
# https://api.line.me/v2/bot/message/reply
