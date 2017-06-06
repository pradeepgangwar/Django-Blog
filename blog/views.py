# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(author__username='pradeep').order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	refer = request.META.get('HTTP_REFERER')
	return render(request, 'blog/post.html', {'post': post, 'refer': refer})

def post_new(request):
	refer = request.META.get('HTTP_REFERER')
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
          	post.author = request.user
           	post.published_date = timezone.now()
           	post.save()
           	return redirect('post_detail', pk=post.pk)
	else:
	    form = PostForm()
	return render(request, 'blog/post_new.html', {'form': form, 'refer': refer})
