# MODELS (M in MVC)
from django.db import models

class Line(models.Model):
    text = models.CharField(max_length=255)


# VIEWS (V in MVC)
from django.shortcuts import render_to_response
from models import Line

def foo(request,):
    return render_to_response("url/to/template.html",
                               {"lines" : Line.objects.all()})


# Controller (C in MVC)
from django.conf.urls import url
from .views import foo

urlpatterns = patterns('',
    url(r'^$', foo),
)