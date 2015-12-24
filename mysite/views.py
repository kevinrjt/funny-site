from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Good Good Study!</h1><br\><h1>Day Day Up!</h1>")
