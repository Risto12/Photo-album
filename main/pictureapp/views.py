from django.shortcuts import render, redirect
from .models import Picture, Request, PictureGroup, PictureGroupUsers
from .form import PictureForm, LogInForm
from django.conf import settings
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout


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


def log_in(request):
	context = {}
	if request.method == 'POST':
		form = LogInForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['user_name'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)
				return redirect(get_all_pictures)
			else:
				context['form'] = LogInForm()
				context['message'] = "User or password invalid"
	else:
		context['form'] = LogInForm()
	return render(request, 'login.html', context)


@permission
def log_out(request):
	logout(request)
	return redirect(log_in)


@permission
@super_user
def add_pic(request):
	if request.method == 'POST':
		form = PictureForm(request.POST, request.FILES)
		if form.is_valid():
			print(form.cleaned_data['group_id'])
			try:
				pic_group = PictureGroup.objects.get(name=form.cleaned_data['group_id'])
				Picture(name=form.cleaned_data['name'], photo=form.cleaned_data['photo'], description=form.cleaned_data['description'],
						picture_group=pic_group).save()
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
	user_id = request.user.id
	pic_group = []
	pic_group_user = PictureGroupUsers.objects.filter(user=user_id).values()
	for i in pic_group_user:
		pic_group.append(i.get('group_id'))
	pics = Picture.objects.filter(picture_group_id__in=pic_group)
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





