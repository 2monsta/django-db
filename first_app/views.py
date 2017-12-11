# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

# def index(req):
# 	my_dictionary = {'insert_content': "Hello world"}
# 	return render(req,'first_app/index.html',context=my_dictionary)


def index(request):
	my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
	# Make sure this is pointing to the correct index
	return render(request,'first_app/index.html',context=my_dict)