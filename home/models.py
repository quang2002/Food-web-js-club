from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likeIds = models.TextField()
    image = models.ImageField(null=True, upload_to='photo/')