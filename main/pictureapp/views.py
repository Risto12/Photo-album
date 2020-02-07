from django.shortcuts import render
from .models import Picture
from .form import PictureForm
from django.conf import settings


def index(request):
	context = {"message": "Hello world" }
	return render(request, 'index.html', context)

def add_picture(request):
	if request.method == 'POST':
		form = PictureForm(request.POST, request.FILES)
		if form.is_valid():
			Picture(name=form.cleaned_data['name'], photo=form.cleaned_data['photo']).save()
			return render(request, 'index.html', {'message': 'Thank you'})
	else:
		form = PictureForm()
	return render(request, 'picture_form.html', {'form': form})


def get_all_pictures(request):
	pics = Picture.objects.all()
	context = {'pics': []}
	for pic in pics:
		print(settings.MEDIA_URL)
		pic.photo = settings.MEDIA_URL + str(pic.photo)
		context['pics'].append({'name':pic.name, 'pic': pic.photo})
	return render(request, 'pictures.html', context)


def clear_db(request):
	Picture.objects.all().delete()
	return render(request, 'index.html', {"message": "clear"})


def get_picture(request):
	return render(request, 'index.html', {'message': ''})


def generic_resp(request):
	return render(request, 'index.html', {'message': 'Thank you'})