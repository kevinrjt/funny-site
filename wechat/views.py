import time
import hashlib
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View

class WeChatInterfaceView(View):
    def get(self, request):
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)

        token = 'kevinmessiren'

        tmpList = [token, timestamp, nonce]
        tmpList.sort()
        tmpstr = '%s%s%s' % tuple(tmpList)
        tmpstr = hashlib.sha1(tmpstr).hexdigest()
        if tmpstr == signature:
            return render(request, 'get.html', {'str': echostr}, content_type='text/plain')

    def post(self, request):
        soup = BeautifulSoup(request.body, "html.parser")
        fromUserName = soup.fromusername.text
        toUserName = soup.tousername.text
        createTime = soup.createtime.text
        msgType = soup.msgtype.text
        content = soup.content.text
        msgId = soup.msgid.text
        return render(request, 'reply_text.xml',
                      {'toUserName': fromUserName,
                       'fromUserName': toUserName,
                       'createTime': time.time(),
                       'msgType': msgType,
                       'content': content},
                      content_type = 'application/xml'
        )
