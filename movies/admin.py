from django.contrib import admin
from django import forms
from .models import *
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget)
    #poster = forms.CharField(label="Постер", widget=CKEditorUploadingWidget)

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1                     # дополнительное пустое поле для отзыва
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
    actions = ['publish', 'unpublish'] # снять/добавить галочку черновик и опубликовать несколько или снять с публикации
    save_as = True
    form = MovieAdminForm
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

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = 'Обновлена 1 запись'
        elif 1 < row_update < 5:
            message_bit = f'Обновлено {row_update} записи'
        else:
            message_bit = f'Обновлено {row_update} записей'
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == '1':
            message_bit = 'Обновлена 1 запись'
        elif 1 < row_update < 5:
            message_bit = f'Обновлено {row_update} записи'
        else:
            message_bit = f'Обновлено {row_update} записей'
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    unpublish.short_description = "Снять с публикации"
    publish.allowed_permissions = ('change',)
    unpublish.allowed_permissions = ('change',)



@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')


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


# Шапка админ-панели, где было написано Администрирование django #
admin.site.site_title = "Администрирование КиноSearch"
admin.site.site_header = "КиноSearch"
#
