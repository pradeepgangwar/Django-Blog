# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(author__username='pradeep').order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
