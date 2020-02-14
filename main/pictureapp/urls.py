from django.urls import path
from . import views

urlpatterns = [
	path('', views.get_all_pictures, name='all_pics'),
	path('get_pic', views.get_picture, name='get_pic'),
	path('add_pic', views.add_pic, name='add_pic'),
	path('req_pic', views.req_pic, name='request_picture'),
	path('delete/<int:pk>', views.del_pic, name='delete'),
	path('log_in', views.log_in, name='log_in'),
	path('log_out', views.log_out, name='log_out'),
]

