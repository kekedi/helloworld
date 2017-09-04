from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime
# Create your views here.
def homepage(request):
	template=get_template('index.html')
	post=Post.objects.all()
	now=datetime.now()
	html=template.render(locals())
	return HttpResponse(html)