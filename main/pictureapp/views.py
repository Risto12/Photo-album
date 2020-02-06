from django.shortcuts import render
from .models import Car, Picture
from .form import PictureForm


def index(request):
	context = {"message": "Hello world" }
	return render(request, 'index.html', context)


def add_car(request):
	Car(name="chevy").save()
	return render(request, 'index.html', {"message": "Saved"})


def get_car(request):
	chevy = Car.objects.get(name="chevy")
	print(chevy.name)
	return render(request, 'index.html', {"message": chevy.name})


def add_picture(request):
	if request.method == 'POST':
		form = PictureForm(request.POST, request.FILES)
		if form.is_valid():
			Picture(name=form.cleaned_data['name'], photo=form.cleaned_data['photo']).save()
			return render(request, 'index.html', {'message': 'Thank you'})
	else:
		form = PictureForm()
	return render(request, 'picture_form.html', {'form': form})

def get_list_of_pictures(request):
	pics = Picture.objects.all()
	for pic in pics:
		print(pic.name)
		print(pic.photo)
	return generic_resp(request)

def get_first_pic(request):
	pass

def clear_db(request):
	Picture.objects.all().delete()
	return render(request, 'index.html', {"message":"clear"})


def get_picture(request):
	return render(request, 'index.html', {'message':''})


def generic_resp(request):
	return render(request, 'index.html', {'message': 'Thank you'})