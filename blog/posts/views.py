from django.shortcuts import *
from django.http import HttpResponse
from django.template import RequestContext, loader
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required

def detail(request,id):
    post = Post.objects.get(id=id)
    return render_to_response('posts/detail.html',{"post":post},context_instance=RequestContext(request))

@login_required
def add_entry(request):
    entry_form = PostForm
    if request.method == 'POST':
        entry = PostForm(request.POST or None)
        if entry.is_valid():
            new_entry = entry.save(commit=False)
            new_entry.save()
            return HttpResponseRedirect('/')
    return render_to_response('posts/add_entry.html',{"entry_form":entry_form},context_instance=RequestContext(request))

@login_required
def edit_entry(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        new_post = PostForm(request.POST or None, instance=post)
        if new_post.is_valid():
            newest_post = new_post.save(commit=False)
            newest_post.save()
            return HttpResponsePermanentRedirect('/posts/detail/%s/' %post.id)
    return render_to_response('posts/edit_entry.html',locals(), context_instance=RequestContext(request))

@login_required
def delete_entry(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return HttpResponsePermanentRedirect('/')
