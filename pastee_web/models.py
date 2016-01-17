from django.db import models
import string, random


class Paste(models.Model):
    paste_name = models.TextField()
    created_at = models.DateTimeField('Created at')

    def __str__(self):
        return self.paste_name
