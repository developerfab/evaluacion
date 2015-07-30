from django.conf.urls import patterns, url
from evaluacion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^crearWorkSpace/$',views.createWorkSpace, name="crearWorkSpace"),
    url(r'^consultaWorkSpace/$', views.consultWorkSpace, name="consultaWorkSpace"),
)