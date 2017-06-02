# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.shortcuts import render

# Create your views here.

def post_list(request):
	post = Post.objects.order_by('published_date')
	return render(request, 'blog/post_list.html', {post})