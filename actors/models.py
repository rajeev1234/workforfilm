from django.db import models

from django.conf import settings
from django.urls import reverse
from financials.models import Financial
from profileprojects.models import ProfileProject
from portfolioelements.models import PortfolioElement


# Create your actorss here.


class Actor(models.Model):
    Actor_Body_Type_choices = (
        ('THIN', 'Thin'),
        ('SLIM', 'Slim'),
        ('ATHLETIC', 'Athletic'),
        ('HEALTHY', 'Healthy'),
        ('HEAVY', 'Heavy'),
        ('BULKY', 'Bulky'),
    )
    Actor_Skin_Color_choices = (
        ('WHITE,FAIR', 'White,Fair'),
        ('MEDIUM,WHITE TO LIGHT BROWN', 'Medium,White To Light Brown'),
        ('OLIVE,MODERATE BROWN', 'Olive,Moderate Brown'),
        ('BROWN,DARK BROWN', 'Brown,Dark Brown'),
        ('BLACK,DARK', 'Black,Dark'),
    )
    Actor_Eye_Color_choices = (
        ('AMBER', 'Amber'),
        ('BLUE', 'Blue'),
        ('BROWN', 'Brown'),
        ('GRAY', 'Gray'),
        ('GREEN', 'Green'),
        ('HAZEL', 'Hazel'),
        ('RED AND VIOLET', 'Red And Violet'),

    )
    Actor_SceneComfort_choices = (
        ('COVERED', 'Covered'),
        ('SEMI NUDE', 'Semi Nude'),
        ('UNDER GARMENTS/BIKINE', 'Under Garments/Bikini'),
        ('FRONTAL NUDE', 'Frontal Nude'),
        ('NUDE', 'Nude'),

    )
    Actor_Favorite_Acting_Styles_Choices = (
        ('Uta Hagen','Uta Hagen'),
        ('Herbert Berghof','Herbert Berghof'),
        ('Leestrasberg','Leestrasberg'),
        ('Sandy Meisner','Sandy Meisner'),
        ('Stella Adler','Stella Adler'),
        ('Alexander Technique','Alexander Technique'),
        ('Method Acting','Method Acting'),
        ('Stanislavsky','Stanislavsky'),
        ('Michael Chekhov','Michael Chekhov'),
        ('other','other ')

    )
    Actor_Ethnicity_Choices = (
        ('Indian','Indian'),
        ('Dravidian','Dravidian'),
        ('Tamils','Tamils'),
        ('Malayali','Malayali'),
        ('Kannada','Kannada'),
        ('Naga','Naga'),
        ('Bengalis','Bengalis'),
        ('Munda','Munda'),
        ('Arabs','Arabs'),
        ('parsi','parsi'),
        ('Dogra','Dogra'),
        ('Kashmiris','Kashmiris'),
        ('Non-resident Indian and Person of Indian Origin','Non-resident Indian and Person of Indian Origin'),
        ('Mizo','Mizo'),
        ('Tais','Tais'),
        ('Sindhis','Sindhis'),
        ('Romani','Romani'),
        ('Telugu','Telugu'),
        ('East Indians','East Indians'),
        ('Sikkimese','Sikkimese'),
        ('odia','odia'),
        ('khasi','khasi'),
        ('Chakma','Chakma'),
        ('Meitei','Meitei'),
        ('Marwari','Marwari'),
        ('Irula','Irula'),
        ('White','White'),
        ('Dardic','Dardic'),
        ('Khonds','Khonds'),
        ('Luso-Indian','Luso-Indian'),
        ('Tibetan','Tibetan'),
        ('Tharu','Tharu'),
        ('Anglo-Indian','Anglo-Indian'),
        ('Garhwali','Garhwali'),
        ('Arab','Arab'),
        ('Black','Black'),
        ('Afro American','Afro American'),
        ('Russian','Russian'),
        ('European','European'),
        ('American','American'),
        ('Australian','Australian'),
        ('Others','Others'),

    )
    Actor_User = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='actors_Creator', on_delete=models.CASCADE)
    Actor_Modified_Date = models.DateTimeField(auto_now=True)
    Actor_Created_Date = models.DateTimeField(auto_now_add=True)

    Actor_Body_Type = models.CharField(max_length=100,choices=Actor_Body_Type_choices)

    Actor_Ethnicity = models.CharField(max_length=100,choices=Actor_Ethnicity_Choices)
    Actor_Eye_Color = models.CharField(max_length=100,choices=Actor_Eye_Color_choices)
    Actor_Favorite_Acting_Styles = models.CharField(max_length=100,choices=Actor_Favorite_Acting_Styles_Choices)
    Actor_Height = models.CharField(max_length=100)
    Actor_Language = models.CharField(max_length=100)
    Actor_SceneComfort = models.CharField(max_length=100,choices=Actor_SceneComfort_choices)
    Actor_Skin_Color = models.CharField(max_length=100,choices=Actor_Skin_Color_choices)
    Actor_Smoker = models.BooleanField(default=False)
    Actor_Special_skill = models.TextField(max_length=500)
    Actor_Weight = models.CharField(max_length=100)
    Actor_Description = models.TextField(max_length=100)

   # Actor_Rating = models.ForeignKey(Rating,related_name='actors',on_delete=models.CASCADE)
   #  Actors_Portfolio= models.ForeignKey(PortfolioElement,related_name='actors',on_delete=models.CASCADE,null=True)
   #  Actors_profileproject = models.ForeignKey(ProfileProject, related_name='actors',on_delete=models.CASCADE,null=True)
    # Actor_Financials = models.ForeignKey(Financial, related_name='Financial', on_delete=models.CASCADE,null=True)




    #Actors_video = models.ForeignKey(video,related_name='actors',on_delete=models.CASCADE)

    def __str__(self):
        return self.Actor_Weight

    def get_absolute_url(self):
        return reverse('actors_details', args=[str(self.id)])