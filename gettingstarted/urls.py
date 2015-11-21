from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import base.views as _V

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', _V.index, name='index'),
    url(r'^db', _V.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
