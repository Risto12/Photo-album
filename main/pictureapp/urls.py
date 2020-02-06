from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('add', views.add_car, name="add"),
	path('get', views.get_car, name="get"),
	path('picture', views.add_picture, name="add_pic"),
	path('del', views.clear_db, name="del"),
	path('all', views.get_list_of_pictures, name='all'),
	path('get_pic', views.get_first_pic, name='get_pic'),
	path('get_info', views.get_info, name='info'),
]
