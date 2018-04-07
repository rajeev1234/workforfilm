from django.db import models

from django.conf import settings

from django.urls import reverse




# Create your portfolio_elements here.


class PortfolioElement(models.Model):
    PortfolioElement_User = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='portfolio_element',on_delete=models.CASCADE)
    PortfolioElement_Created_Date = models.DateTimeField(auto_now_add=True)
    PortfolioElement_Updated_Date = models.DateTimeField(auto_now=True)

    PortfolioElement_VideoAudio = models.FileField()
    PortfolioElement_Image = models.ImageField(max_length=200)

    PortfolioElement_Title = models.CharField(max_length=200)
    PortfolioElement_Category = models.CharField(max_length=200)
    PortfolioElement_Director = models.CharField(max_length=200)
    PortfolioElement_Production_House = models.CharField(max_length=200)
    portfolioElement_Message = models.CharField(max_length=200)


    def __str__(self):
        return self.PortfolioElement_Category

    def get_absolute_url(self):
        return reverse('portfolio_element_details', args=[str(self.id)])


