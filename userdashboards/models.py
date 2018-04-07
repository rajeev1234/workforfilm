from django.db import models
from django.conf import settings

# Create your models here.


class UserDashBoard (models.Model):

    UserDashBoard_User = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='UserDashBoard', on_delete=models.CASCADE)
    UserDashBoard_Talent = models.BooleanField(default=False)
    UserDashBoard_Crew = models.BooleanField(default=False)
    UserDashBoard_Producer = models.BooleanField(default=False)
    UserDashBoard_Service_Provider = models.BooleanField(default=False)
