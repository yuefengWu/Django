# coding=utf-8
from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse("hello");


def showTime(request):
    now = datetime.datetime.now()
    html = """<html><body>It is now %s.
    <div id='mybtn'><input type='button' value='click me'></div></body></html>""" % now
    return HttpResponse(html)


def showCurrentTime(request):
    now = datetime.datetime.now()
    html = """<html><body><div id="timeArea"></div></body><script>function
    getTime(){document.getElementById('timeArea').innerText='%s';}setInterval("getTime()",1000);</script></html>""" % now
    return HttpResponse(html)


def showPicture(request):
    image_data = open("1.png", "rb").read()
    return HttpResponse(image_data, content_type = "image/png")
