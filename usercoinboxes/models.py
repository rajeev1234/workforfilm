from django.db import models

# Create your models here.


class UserCoinBox(models.Model):
    UserCoinBox_Freemium_Coin = models.IntegerField()
    UserCoinBox_Pro_Coin = models.IntegerField()