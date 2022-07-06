from django.contrib import admin

from home.models import *

# Register your models here.
# class HomeAdmin(admin.ModelAdmin):
# list_display = ('name', 'email')


admin.site.register(movies)
admin.site.register(ticket)
admin.site.register(cinema_house)
admin.site.register(movie_price_cinema)
admin.site.register(users)
