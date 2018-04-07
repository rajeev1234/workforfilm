from django.db import models

# Create your models here.


class Financial(models.Model):
    Financial_Available = models.BooleanField(default=False)
    Financial_Crew_Size_Negotiablity = models.BooleanField(default=False)
    #Financial_Charges_Negotiable = models.BooleanField(default=False)
    Financial_Duration_Negotiablity = models.BooleanField(default=False)

    Financial_Crew_Size_Negotiablity_student = models.IntegerField()
    Financial_Crew_Size_Negotiablity_TV = models.IntegerField()
    Financial_Crew_Size_Negotiablity_Film = models.IntegerField()

    Financial_Daily_Charges = models.IntegerField()
    Financial_Weekly_Charges = models.IntegerField()
    Financial_Montly_Charges = models.IntegerField()

    Financial_Negotiated_Charges = models.IntegerField()

