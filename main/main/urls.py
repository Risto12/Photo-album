from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

settings.MEDIAL_URL = '/home/risto/projektit/pictureapp/main/pictures/'
settings.MEDIA_ROOT = '/home/risto/projektit/pictureapp/main/pictures/'

urlpatterns = [
   path('', include('pictureapp.urls')),
	path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
