from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject_cms_templates.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/$', 'cms_templates.views.usuario'),
    url(r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout$','django.contrib.auth.views.logout'),
    url(r'^/?pages$', 'cms_templates.views.obtener_lista'),
    url(r'^/?annotated/pages$', 'cms_templates.views.obtener_lista_annotated'),
    url(r'^/?(\d+)$', 'cms_templates.views.id_to_page'),
    url(r'^/?annotated/(\d+)$', 'cms_templates.views.id_to_page_annotated'),
    url(r'/?annotated/(.*)', 'cms_templates.views.name_to_page_annotated'),
    url(r'/?(.*)', 'cms_templates.views.name_to_page'),
)
