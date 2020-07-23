from django.db import models


class Categories(models.Model):
    """Categories"""
    name = models.CharField("categories", max_length=150, unique=True)
    icon = models.ImageField("icon")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Levels(models.Model):
    """Levels"""
    LEVELS = [
        ("A1", "A1"),
        ("A2", "A2"),
        ("B1", "B1"),
        ("B2", "B2"),
        ("C1", "C1"),
        ("C2", "C2"),
    ]
    name = models.CharField("levels", max_length=150, unique=True)
    code = models.CharField("level code", choices=LEVELS, max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"


class Theme(models.Model):
    categories = models.ForeignKey(Categories, related_name='categories_to_theme',
                                   verbose_name='theme_categories_verbose', on_delete=models.CASCADE)
    levels = models.ForeignKey(Levels, related_name='levels_to_theme',
                               verbose_name='theme_levels_verbose', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=150, unique=True)
    photo = models.ImageField('photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"


class Words(models.Model):
    name = models.CharField('name', max_length=150, unique=True)
    translation = models.TextField('translation')
    transcription = models.TextField('transcription')
    example = models.TextField('example')
    sound = models.FileField('sound')
    theme = models.ForeignKey(Theme, related_name='words_to_theme',
                              verbose_name='words_theme_verbose', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Word"
        verbose_name_plural = "Words"


