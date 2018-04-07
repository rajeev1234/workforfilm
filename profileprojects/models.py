from django.db import models

from django.conf import settings
from django.urls import reverse


# Create your ProfileProjects here.


class ProfileProject(models.Model):
    ProfileProject_User = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ProfileProjects',
                                            on_delete=models.CASCADE)
    ProfileProject_Created_Date = models.DateTimeField(auto_now_add=True)
    ProfileProject_Updated_Date = models.DateTimeField(auto_now=True)

    ProfileProject_Image = models.ImageField()
    Profile_Project_Video = models.FileField()

    ProfileProject_Category = models.CharField(max_length=200)
    ProfileProject_Director = models.CharField(max_length=200)
    ProfileProject_Production_House = models.CharField(max_length=200)
    ProfileProject_Title = models.CharField(max_length=200)



    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('ProfileProjects_details', args=[str(self.id)])

