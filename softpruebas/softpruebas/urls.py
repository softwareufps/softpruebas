from django.conf.urls import include, url
from django.contrib import admin
from appprueba import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'softpruebas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
     url(r'^hola/$',views.vistasqli),
]
