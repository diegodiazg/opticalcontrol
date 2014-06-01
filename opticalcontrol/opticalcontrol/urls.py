from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opticalcontrol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
     url(r'^$','django.contrib.auth.views.login',
      {'template_name':'inicio.html'}, name='login'),

      url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',
       name='logout'),


   # url(r'^$','pos.views.inicio'),
    url(r'^productos/$','pos.views.productos'),
    url(r'^cliente/$','pos.views.clientes'),
    url(r'^cliente/nuevo/$','pos.views.cliente_nuevo'),
    url(r'^contacto/$','pos.views.contacto'),
    url(r'^productos/nuevo/$','pos.views.agregar_producto'),
    url(r'^ventas/$','pos.views.ventas'),
    url(r'^busqueda_cliente/$','pos.views.busqueda_cliente'),
    url(r'^busqueda_producto/$','pos.views.busqueda_producto'),
     url(r'^formulario/$','pos.views.formulario'),
)

