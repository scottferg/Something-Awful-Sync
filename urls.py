from django.conf.urls.defaults import *
from django.contrib import admin

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from bookmarks.handler import *

auth = {
    'authentication': HttpBasicAuthentication(realm = 'sa-bookmark-sync')
}

admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^api/v1/user/$', Resource(handler = UserHandler)),
    (r'^api/v1/bookmark/(?P<bookmark_id>[^/]+)/$', Resource(handler = SyncByIdV1Handler, **auth)),
    (r'^api/v1/bookmark/$', Resource(handler = SyncV1Handler, **auth)),

    (r'^admin/', include(admin.site.urls)),
)
