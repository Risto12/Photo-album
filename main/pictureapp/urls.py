from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.index, name='index'),
	path('picture', views.add_picture, name="add_pic"),
	path('del', views.clear_db, name="del"),
	path('all_pics', views.get_all_pictures, name='all_pics'),
]

