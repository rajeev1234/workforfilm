from django.db import models
from django.conf import settings

# Create your models here.


class Talent(models.Model):

    Talent_User = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Talent', on_delete=models.CASCADE)

    Talent_Actor = models.BooleanField(default=False)
    Talent_Child_Artist = models.BooleanField(default=False)
    Talent_Dancer = models.BooleanField(default=False)
    Talent_Mimicry_Artist = models.BooleanField(default=False)
    Talent_Models = models.BooleanField(default=False)
    Talent_Musician = models.BooleanField(default=False)
    Talent_Singer = models.BooleanField(default=False)
    Talent_Special_Art = models.BooleanField(default=False)
    Talent_Theater_Artist = models.BooleanField(default=False)
    Talent_Voice_Over_Artist = models.BooleanField(default=False)

