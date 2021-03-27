#
from model_utils.models import TimeStampedModel
#
from django.db import models

class Video(TimeStampedModel):
    """  Modelo para almacenar videos a reproducir  """

    title = models.CharField(
        'title', 
        max_length=255,
        blank=True
    )
    url = models.URLField(
        blank=False, 
        null=True
    )
    image = models.CharField(
        'imagen',
        max_length=500,
        blank=True,
    )


    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
    
    def __str__(self):
        return self.title