from django.conf.urls import url
from . import views

urlpatterns = [
	# example: /items/
	url(r'^$', views.index, name='index'),
	# example: /items/34
	url(r'(?P<item_id>[0-9]+)/$', views.detail, name='detail')
]