from django.db import models
from django.conf import settings

class Note(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=200)
    created_ad = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title