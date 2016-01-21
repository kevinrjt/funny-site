#coding:utf-8

import authority

import ast, time, urllib

from bs4 import BeautifulSoup
from django.shortcuts import render
from django.views.generic.base import View

class WeChatInterfaceView(View):
    def get(self, request):
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        if authority.validate(signature, timestamp, nonce):
            return render(request, 'get.html', {'str': echostr}, content_type='text/plain')

    def post(self, request):
        soup = BeautifulSoup(request.body, "html.parser")
        fromUserName = soup.fromusername.text
        toUserName = soup.tousername.text
        createTime = soup.createtime.text
        msgType = soup.msgtype.text
        msgId = soup.msgid.text

        replyContent = ''

        if msgType == 'text':
            content = soup.content.text
            try:
                replyContent = str(eval(content))
            except Exception:
                replyContent = content[::-1]
        elif msgType == 'image':
            replyContent = '1234567890'
        else:
            replyContent = msgType
        return render(request, 'reply_text.xml',
                      {'toUserName': fromUserName,
                       'fromUserName': toUserName,
                       'createTime': time.time(),
                       'content': replyContent
                      },content_type = 'application/xml'
                     )
