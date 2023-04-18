from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include("django.conf.urls.i18n")),
    path('', include('api.urls'))
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
