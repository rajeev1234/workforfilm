from django.contrib import admin

# Register your models in admin panels here.

from . import models



# calling in admin panel


admin.site.register(models.PortfolioElement)

