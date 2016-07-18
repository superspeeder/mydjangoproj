from django.conf.urls import url
import views

urlpatterns = [
        url('^index/(?P<indexn>[0-9]+)', views.index),
        url('^owner', views.owner_contact),
        url("^search/emailaddr=(?P<queryval>'[0-9a-zA-Z_\.]+@[0-9a-zA-Z_\.]+')", views.searchemail),
        url("^search/(?P<querytype>[a-zA-Z]+)=(?P<queryval>'[a-zA-Z_]+')", views.search),

]
