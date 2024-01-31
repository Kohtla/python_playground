from django.http import HttpResponse
import time


def index(request):
    time.sleep(0.1)
    return HttpResponse()
