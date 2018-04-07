from django.db import models


from django.conf import settings

from django.urls import reverse
from profileprojects.models import ProfileProject

# Create your bookings here.


class Booking(models.Model):
    Booking_User = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='creator_bookings', on_delete=models.CASCADE)
    Booking_Modified_Date = models.DateTimeField(auto_now=True)
    Booking_Created_Date = models.DateTimeField(auto_now_add=True)

    Booking_For_User=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='For_Booking',on_delete=models.CASCADE)
    Booking_Project=models.ForeignKey(ProfileProject,related_name='Booking',on_delete=models.CASCADE)
    Booking_Status = models.CharField(max_length=100)
    Booking_Charges_After_Negotiable=models.CharField(max_length=100)
    Booking_From_Date=models.DateField()
    Booting_Till_Date=models.DateField()



    def __str__(self):
        return self.Booking_Status

    def get_absolute_url(self):
        return reverse('booking_details', args=[str(self.id)])


# Create bookings Comments here.


class Comment(models.Model):

    Booking_Comment = models.CharField(max_length=150, null=False)
    Comment_Booking = models.ForeignKey(Booking, null=False,related_name="Comment_Bookingnew", on_delete=models.CASCADE)
    Booking_Comment_Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="booking_comment")

    # booking_Comment_Created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Booking_Comment

    def get_absolute_url(self):
        return reverse('booking_list')

