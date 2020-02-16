from django.db import models
from django.contrib.auth.models import User


class PictureGroupTuple(models.Manager):

    def get_choises(self):
        groups = self.all().values()
        choises = []
        for group in groups:
            choises.append((group.get('name'), group.get('name')))
        return choises


class PictureGroup(models.Model):

    name = models.CharField(max_length=100, primary_key=True)

    objects = models.Manager()
    choises = PictureGroupTuple()

    class Meta:
        db_table = "pic_grp"


class Picture(models.Model):

    name = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='pictures', unique=True)
    description = models.TextField(null=True)
    picture_group = models.ForeignKey(PictureGroup, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "pic"


class PictureGroupUsers(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(PictureGroup, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "pic_grp_user"


class Request(models.Model):

    time = models.DateField(auto_now_add=True)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "request"


