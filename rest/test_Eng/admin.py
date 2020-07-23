from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Categories, Words, Theme, Levels

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "icon")
    list_display_links = ("name",)
    readonly_fields = ["preview_image"]

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.icon.url,
            width=obj.icon.width,
            height=obj.icon.height,
        )
        )


@admin.register(Levels)
class LevelsAdmin(admin.ModelAdmin):
    """Levels"""
    list_display = ("id","name", "code")
    list_display_links = ("name",)


@admin.register(Theme)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id","name", "photo",)
    list_display_links = ("name",)
    readonly_fields = ["preview_image"]

    def preview_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=obj.photo.width,
            height=obj.photo.height,
        )
        )


@admin.register(Words)
class CategoryAdmin(admin.ModelAdmin):
    """Words"""
    list_display = ("id","name", "translation", "transcription", "example","sound")
    list_display_links = ("name",)
