from django.conf import settings
from django.db import models
from django.utils.deconstruct import deconstructible
import uuid
import os

@deconstructible
class PathAndRename(object):
    """ To be called when uploading new media. Renames file to UUID."""
    
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext  = filename.split('.')[-1]
        filename = f'{uuid.uuid4().hex}.{ext}'
        return os.path.join(self.path, filename)

class Foto(models.Model):
    """Keeps information about uploaded media file."""
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to= PathAndRename('fotos/'))
    added = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title if self.title else self.image.url

    def get_image_url(self):
        return f"{settings.MEDIA_URL}/{self.image}"
