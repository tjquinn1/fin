from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='capm_home'),
    url(r'^capm_list/$', views.capm_list, name='capm_list'),
    url(r'^new/$', views.add_capm, name='capm_form'),
    url(r'^capm_list/(?P<capm_id>[0-9]+)/$', views.capm_detail, name='detail'),

]