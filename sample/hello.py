from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.template import Context, Template

def hello_world(request):
#    template = loader.get_template("hello.html")
    c = Context({"variable": "World"})
    return render_to_response("hello.html", {"variable": "World"})