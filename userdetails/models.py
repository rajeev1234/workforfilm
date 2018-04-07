from django.db import models

from django.conf import settings

from django.urls import reverse

# Create your userdetails here.


class UserDetails(models.Model):

    UserDetail_User = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='UserDetails', on_delete=models.CASCADE)
    UserDetail_Created_Date = models.DateTimeField(auto_now_add=True)

    UserDetail_First_Name = models.CharField(max_length=200)
    UserDetail_Last_Name = models.CharField(max_length=200)
    UserDetails_Phone = models.IntegerField()

    UserDetail_Date_Of_Birth = models.DateField()
    UserDetail_Gender = models.CharField(max_length=200)

    UserDetail_Street_Address= models.CharField(max_length=200)
    UserDetail_City = models.CharField(max_length=200)
    UserDetail_State = models.CharField(max_length=200)
    UserDetail_Country = models.CharField(max_length=200)
    UserDetail_Pin_Code = models.IntegerField()

 #   UserDetail_Official_ID = models.ForeignKey(Image, related_name='UserDetails',on_delete=models.CASCADE)
    UserDetail_Profile_Picture = models.ImageField()

    UserDetail_User_Description = models.CharField(max_length=200)

    UserDetail_Completed = models.BooleanField(default=True)

    def __str__(self):
        return self.UserDetail_First_Name

    def get_absolute_url(self):
        return reverse('userdetails_details', args=[str(self.id)])