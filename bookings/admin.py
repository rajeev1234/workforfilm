from django.contrib import admin

# Register your models in admin panels here.

from . import models

# declaring comments stack


admin.site.register(models.Booking)

