from django.db import models

# Create your models here.

UserProfessionalInfo_Bank_Account_Name = models.CharField(max_length=200, unique=True)
UserProfessionalInfo_Bank_Account_Number = models.IntegerField()
UserProfessionalInfo_Bank_Name = models.CharField(max_length=200)
UserProfessionalInfo_Bank_Account_Type = models.CharField(max_length=200)
UserProfessionalInfo_Bank_Account_IFSC_Code = models.CharField(max_length=20)