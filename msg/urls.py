from django.conf.urls import include, url
from msg import views

#url dispatcher
#urlpatterns = patterns('', url(r'^$', views.index, name="index"))

urlpatterns = [
    url(r'^$', views.index, name="index")
]