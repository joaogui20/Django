from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField

# Create your models here.
class Category(models.Model):
   nome = models.CharField(max_length=255)

   def __str__(self):
       return self.nome

   def get_absolute_url(self): #url name
       return reverse('home')

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=255, default="Reitoria")
    post_data = models.DateTimeField(auto_now_add=True)
  
    corpo = RichTextUploadingField(blank=True, null=True)
    imagem = models.ImageField(null=True, blank=True, upload_to='images/')
    arquivo = models.FileField(null=True, blank=True, upload_to='files/')
    youtube = EmbedVideoField(null=True, blank=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self): 
        return reverse('home') 