from django.contrib import admin
from django.urls import include, path

urlpatterns = [
   path('pictures/', include('pictureapp.urls')), 
	path('admin/', admin.site.urls),
]
