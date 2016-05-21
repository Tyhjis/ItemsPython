from django.conf.urls import url
from . import views

app_name = 'stuffdb'
urlpatterns = [
	# example: /items/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# example: /items/34
	url(r'(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# example: /items/34/update
	url(r'(?P<item_id>[0-9]+)/update/$', views.update, name='update')
]