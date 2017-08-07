from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^', include('user_auth.urls')),
    url(r'^', include('landings.urls')),
    # url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^clients/', include('clients.urls')),
    url(r'^irsexpress/', include('irs_common.urls')),
    url(r'^agents/', include('agents.urls')),
    url(r'^repo/', include('repository.urls')),
    # url(r'^clients/', include('irs433a.urls')),
    # url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^adminweb/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': 'static'
    })
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
