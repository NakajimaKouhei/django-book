from django.conf.urls import include, url
from django.contrib import admin 

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('user.urls', namespace='user')),
    url(r'^book/', include('book.urls', namespace='book')),
]
