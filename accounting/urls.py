from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^books/', include('accounting.apps.books.urls',
        namespace="books")),
    url(r'^people/', include('accounting.apps.people.urls',
        namespace="people")),
    url(r'^reports/', include('accounting.apps.reports.urls',
        namespace="reports")),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
