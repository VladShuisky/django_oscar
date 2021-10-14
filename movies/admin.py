from django.contrib import admin
from .models import *
models = [Actor, Category, Genre, Movie, MovieShots, RatingStar, Rating, Reviews]
for model in models:
    admin.site.register(model)



# Register your models here.
