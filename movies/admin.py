from django.contrib import admin
from .models import *
from django.utils.html import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 0
    fields = ('get_image', 'description')
    readonly_fields = ('get_image', )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="130" height="110">')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year',)
    search_fields = ('title', 'category__name',)
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    readonly_fields = ('get_image', )
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'), )
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'))
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

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="110" height="110" >')

    get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'parent', 'movie', 'id')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src = "{obj.image.url}" width="50" height="60">')

    get_image.short_description = "Изображение"


admin.site.register(Genre)


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_image',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="60">')

    get_image.short_description = "Изображение"

admin.site.register(RatingStar)
admin.site.register(Rating)

# models = [Actor, (Category, CategoryAdmin), Genre, Movie, MovieShots, RatingStar, Rating, Reviews]
# for model in models:
#     admin.site.register(model)

### Шапка админ-панели, где было написано Администрирование django ###
admin.site.site_title = "Администрирование КиноSearch"
admin.site.site_header = "КиноSearch"
######
