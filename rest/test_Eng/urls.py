from django.urls import path

from . import views


urlpatterns = [
    path("categories/", views.CategoriesListView.as_view()),
    path("levels/", views.LevelsListView.as_view()),
    path("words/<int:pk>", views.WordsListView.as_view()),
    path("themes/", views.ThemesListView.as_view()),
    path("themes/<int:pk>/", views.ThemeView.as_view()),
]