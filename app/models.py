# if you want to list/edit/delete uploaded files, then you want to use models

from django.db import models


class UploadFile(models.Model):
    """ models for uploaded file """
    file = models.ImageField('image file')

    def __str__(self):
        """ return file url """
        return self.file.url
