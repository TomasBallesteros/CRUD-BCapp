"""bc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'insumo.views.inicio', name='inicio'),
    url(r'^insumo/nuevo/$','insumo.views.insumoCreation' , name='insumo_nuevo'),
    url(r'^insumo/listado/$','insumo.views.insumoList' , name='insumo_listado'),
    url(r'^insum/(?P<id_codigo>\d+)$','insumo.views.insumoUpdate', name='insumo_detalle'),
    url(r'^insum_e/(?P<id_codigo>\d+)$','insumo.views.insumoDelete', name='insumo_borrar'),
    url(r'^$', 'obra.views.inicio', name='inicio'),
    url(r'^obra/nuevo/$','obra.views.obraCreation' , name='obra_nuevo'),
    url(r'^obra/listado/$','obra.views.obraList' , name='obra_listado'),
    url(r'^obr/(?P<id_nit>\d+)$','obra.views.obraUpdate', name='obra_detalle'),
    url(r'^obr_e/(?P<id_nit>\d+)$','obra.views.obraDelete', name='obra_borrar'),
    url(r'^presupuesto/nuevo/$','presupuesto.views.presupuestoCreation', name='presupuesto_nuevo'),
    url(r'^presupuesto/listado/$','presupuesto.views.presupuestoList', name='presupuesto_listado'),
    url(r'^presupuest/(?P<id_Presupuesto>\d+)$','presupuesto.views.presupuestoUpdate', name='presupuesto_detalle'),
    url(r'^presupuest_e/(?P<id_Presupuesto>\d+)$','presupuesto.views.presupuestoDelete', name='presupuesto_borrar'),
)
