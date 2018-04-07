
from django.conf import settings

from django.urls import reverse

# Create your Ratings here.


from django.db import models

class Rating(models.Model):
    Rating_User= models.ForeignKey(settings.AUTH_USER_MODEL,related_name='rate',on_delete=models.CASCADE,null=True)
    Rating_Create_Date = models.DateTimeField(auto_now_add=True)
    Rating_Modified_Date = models.DateTimeField(auto_now=True)

    Rating = models.IntegerField()

    def __str__(self):
        return self.Rating

    def get_absolute_url(self):
        return reverse('Rating_details', args=[str(self.id)])
