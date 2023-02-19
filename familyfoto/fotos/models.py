from django.conf import settings
from django.db import models

class Foto(models.Model):
    """Keeps information about uploaded media file."""
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='fotos/')
    added = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title if self.title else self.image.url

    def get_image_url(self):
        return f"{settings.MEDIA_URL}/{self.image}"
