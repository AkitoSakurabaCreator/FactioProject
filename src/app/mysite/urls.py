from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls.static import static #EC

from django.views.static import serve  #追加

# import xadmin #xadmin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    # path('xadmin/', xadmin.site.urls),
    #re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    #re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

