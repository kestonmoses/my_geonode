from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from geonode.sitemap import LayerSitemap, MapSitemap
import geonode.proxy.urls

# Import *_signals.py
import geonode.social_signals

# Setup Django Admin
from django.contrib import admin
admin.autodiscover()

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('geonode',)
}

sitemaps = {
    "layer": LayerSitemap,
    "map": MapSitemap
}

urlpatterns = patterns('',

    # Static pages
    url(r'^$', 'django.views.generic.simple.direct_to_template',
                {'template': 'site_index.html'}, name='home'),
    url(r'^help/$', 'django.views.generic.simple.direct_to_template',
                {'template': 'help.html'}, name='help'),
    url(r'^developer/$', 'django.views.generic.simple.direct_to_template',
                {'template': 'developer.html'}, name='developer'),
    url(r'^about/$', 'django.views.generic.simple.direct_to_template',
                {'template': 'about.html'}, name='about'),

    # Layer views
    (r'^layers/', include('geonode.layers.urls')),

    # Map views
    (r'^maps/', include('geonode.maps.urls')),

    # Catalogue views
    (r'^catalogue/', include('geonode.catalogue.urls')),

    # Search views
    (r'^search/', include('geonode.search.urls')),

    # Upload views
    (r'^upload/', include('geonode.upload.urls')),

    # Social views
    (r"^account/", include("account.urls")),
    (r'^people/', include('geonode.people.urls')),
    (r'^avatar/', include('avatar.urls')),
    (r'^comments/', include('dialogos.urls')),
    (r'^ratings/', include('agon_ratings.urls')),
    (r'^activity/', include('actstream.urls')),
    (r'^relationships/', include('relationships.urls')),
    (r'^announcements/', include('announcements.urls')),
    #(r'^notifications/', include('notification.urls')),
    (r'^messages/', include('user_messages.urls')),

    # Accounts
    url(r'^account/ajax_login$', 'geonode.views.ajax_login',
                                       name='account_ajax_login'),
    url(r'^account/ajax_lookup$', 'geonode.views.ajax_lookup',
                                       name='account_ajax_lookup'),

    # Meta
    url(r'^lang\.js$', 'django.views.generic.simple.direct_to_template',
         {'template': 'lang.js', 'mimetype': 'text/javascript'}, name='lang'),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog',
                                  js_info_dict, name='jscat'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
                                  {'sitemaps': sitemaps}, name='sitemap'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^admin/', include(admin.site.urls)),

    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

    url(r'^blog/', include('zinnia.urls')),
    url(r'^djcomments/', include('django.contrib.comments.urls')),
    )

#Documents views
if settings.DOCUMENTS_APP:
    urlpatterns += patterns('',
        (r'^documents/', include('geonode.documents.urls')),
    )

urlpatterns += geonode.proxy.urls.urlpatterns

# Serve static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
