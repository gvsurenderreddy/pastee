from django.db import models


class Language(models.Model):
    name = models.TextField()
    identifier = models.TextField()


class Paste(models.Model):
    paste_name = models.TextField()
    created_at = models.DateTimeField('Created at')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.paste_name
