from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year',)
    search_fields = ('title', 'category__name',)
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    # fields = (("actors", "directors", "genres"), )
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'), )
        }),
        (None, {
            'fields': (('description', 'poster'), )
        }),
        (None, {
            'fields': (('actors', 'directors', 'genres'), )
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'), )
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fess_in_world'), )
        }),
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'parent', 'movie', 'id')



admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)

# models = [Actor, (Category, CategoryAdmin), Genre, Movie, MovieShots, RatingStar, Rating, Reviews]
# for model in models:
#     admin.site.register(model)


