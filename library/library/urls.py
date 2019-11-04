from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('polls/', include('poll.urls')),
    path('members/', include('member.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('static', document_root='../public/static')
    urlpatterns += staticfiles_urlpatterns()