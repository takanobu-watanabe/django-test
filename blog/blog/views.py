from django.shortcuts import *
from django.http import HttpResponse
from django.template import RequestContext, loader
from posts.models import Post

def top(request):
    all_posts = Post.objects.all()
    print 'all_post:%s' %all_posts
    return render_to_response('top.html',{"all_posts":all_posts},context_instance=RequestContext(request))


