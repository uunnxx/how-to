from django.urls import re_path
from django.http import HttpResponse


urlpatterns = [
    re_path(r'^$', lambda request: HttpResponse('Welcome home')),
    re_path(r'^path/$', lambda request: HttpResponse(request.path)),
    re_path(r'^method/$', lambda request: HttpResponse(request.method)),
    re_path(r'^get_host/$', lambda request: HttpResponse(request.get_host()))
]
