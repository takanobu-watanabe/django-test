from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth.views import login,logout
admin.autodiscover()

urlpatterns = (
    url(r'^$', 'blog.views.top',name='top'),
    url(r'^posts/', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login, {'template_name':'login.html'}),
    url(r'^logout/', logout, {'template_name':'logout.html'})
)
