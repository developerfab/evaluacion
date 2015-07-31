from django.conf.urls import patterns, url
from evaluacion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^crearWorkSpace/$',views.createWorkSpace, name="crearWorkSpace"),
    url(r'^consultaWorkSpace/$', views.consultWorkSpace, name="consultaWorkSpace"),
    url(r'^buscarId/$', views.searchWorkSpace, name="buscarId"),
    url(r'^verEspacio/(?P<identificador>\w{0,100})/$', views.seeWorkSpace, name="verEspacio"),
    url(r'^crearFigura/(?P<figura>\w{0,10})/$', views.createFigure, name="crearFigura"),
)