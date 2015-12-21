from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello Nankai Sister!</h1><br\><h1>Hello Chun Yuan!</h1>")
