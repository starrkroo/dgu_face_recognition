from django.db import models

class Accounts(models.Model):
    image = models.ImageField(upload_to='message_image/%Y/%m', null=True)