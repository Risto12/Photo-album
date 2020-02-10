from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.get_all_pictures, name='all_pics'),
	path('get_pic', views.get_picture, name='get_pic'),
	path('add_pic', views.add_pic, name='add_pic'),
	path('del', views.clear_db, name="del"),
	path('req_pic', views.req_pic, name='request_picture'),
	path('cldb', views.clear_db, name="del_db"),
	path('index', views.index, name="index"),
	path('delete/<int:pk>', views.del_pic, name='delete'),
	path('log_in', views.log_in, name='log_in'),
]

