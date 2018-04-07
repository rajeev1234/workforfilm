from django.db import models
from django.conf import settings
from usereducationinfos.models import EducationInfo
from profileprojects.models import ProfileProject

# Create your models here.
class UserProfessionalInfo(models.Model):
    Hometown = (
        ('a', '1'),
        ('b', '2'),
        ('c', '3'),
    )

    Years_Of_Experience = (
        ('a', '1'),
        ('b', '2'),
        ('c', '3'),
    )
    Spoken_Languages = (
        ('a', '1'),
        ('b', '2'),
        ('c', '3'),
    )

    Understandable_Language =(
        ('a', '1'),
        ('b', '2'),
        ('c', '3'),
    )
    Writable_Language=(
        ('a', '1'),
        ('b', '2'),
        ('c', '3'),
    )

UserProfessionalInfo_User = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='UserDetails',
                                              on_delete=models.CASCADE)
UserProfessionalInfo_Hometown = models.FloatField(max_length=200, choices='Hometown')
UserProfessionalInfo_Experienced = models.BooleanField(default=True)
UserProfessionalInfo_Years_Of_Experience = models.IntegerField(choices='Years_Of_Experience')
UserProfessionalInfo_Education = models.ForeignKey(EducationInfo, on_delete=models.CASCADE)
UserProfessionalInfo_Projects_Done = models.ForeignKey(ProfileProject, on_delete=models.CASCADE)
UserProfessionalInfo_Spoken_Languages = models.CharField(max_length=100, choices='Spoken_Languages')
UserProfessionalInfo_Understandable_Language = models.CharField(max_length=100, choices='Understandable_Language')
UserProfessionalInfo_Writable_Language = models.CharField(max_length=200, choices='Writable_Language')
