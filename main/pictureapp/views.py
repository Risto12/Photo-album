from django.shortcuts import render, redirect
from .models import Picture, Request
from .form import PictureForm, LogInForm
from django.conf import settings
from django.db import IntegrityError


def access_denied(request):
	return render(request, 'error.html', {'message': 'Permission denied'})


def permission(func):
	def auth_check(*args, **kwargs):
		if args[0].user.is_authenticated:
			return func(*args, **kwargs)
		else:
			return log_in(*args, **kwargs)
	return auth_check


def super_user(func):
	def super_check(*args, **kwargs):
		if args[0].user.is_superuser:
			return func(*args, **kwargs)
		else:
			return access_denied(*args, **kwargs)
	return super_check


@permission
def index(request):
	if request.user.is_authenticated:
		context = {"message": "Authenticated" }
	else:
		context = {"message": "Not authenticated"}
	return render(request, 'test.html', context)


def log_in(request):
	if request.method == 'POST':
		form = LogInForm(request.POST)
		if form.is_valid():
			try:
				return redirect(get_all_pictures)
			except IntegrityError:
				form = LogInForm()
	else:
		form = LogInForm()
	return render(request, 'login.html', {'form': form})

@permission
@super_user
def add_pic(request):
	if request.method == 'POST':
		form = PictureForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				Picture(name=form.cleaned_data['name'], photo=form.cleaned_data['photo'], description=form.cleaned_data['description']).save()
				return redirect(get_all_pictures)
			except IntegrityError:
				#FIX ERROR MESSAGE
				form = PictureForm()
	else:
		form = PictureForm()
	return render(request, 'picture_form.html', {'form': form})


@permission
@super_user
def del_pic(request, *args, **kwargs):
	pic_pk = kwargs["pk"]
	Picture.objects.filter(id=pic_pk).delete()
	return redirect(get_all_pictures)


@permission
def get_all_pictures(request):
	pics = Picture.objects.all()
	context = {'pics': []}
	for pic in pics:
		pic.photo = settings.MEDIA_URL + str(pic.photo)
		context['pics'].append({'id': pic.id, 'name':pic.name, 'pic': pic.photo, 'description': pic.description})
	return render(request, 'pictures.html', context)


@permission
def get_picture(request):
	pic = Picture.objects.get(name=request.GET["subject"])
	pic.photo = settings.MEDIA_URL + str(pic.photo)
	return render(request, 'picture.html', {'id': pic.id, 'name': pic.name, 'pic': pic.photo, 'description': pic.description})

@permission
def req_pic(request):
	Request().save()
	return render(request, 'index.html', {'message': 'Request has been send'})


@permission
def clear_db(request):
	Picture.objects.all().delete()
	return render(request, 'index.html', {"message": "clear"})


