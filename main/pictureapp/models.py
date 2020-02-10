from django.db import models


class Picture(models.Model):

    name = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='pictures', unique=True)
    description = models.TextField(null=True)

class Request(models.Model):

    time = models.DateField(auto_now_add=True)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, null=True)