from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Categories, Levels, Theme, Words
from .serealizers import CaregoriesSerializer, LevelsSerializer, \
    WordsSerializer,ThemesSerializer, ThemeSerializer


class CategoriesListView(APIView):
    """print categories list"""
    def get(self, request):
        categories = Categories.objects.filter()
        serializer = CaregoriesSerializer(categories,  many=True)
        return Response(serializer.data)



class LevelsListView(APIView):
    """print levels list"""
    def get(self, request):
        levels = Levels.objects.filter()
        serializer = LevelsSerializer(levels,  many=True)
        return Response(serializer.data)


class WordsListView(APIView):
    """print levels list"""
    def get(self, request, pk):
        words = Words.objects.get(id=pk)
        serializer = WordsSerializer(words)
        return Response(serializer.data)


class ThemesListView(APIView):
    """print themes list"""

    def get(self, request):
        themes = Theme.objects.filter()
        serializer = ThemesSerializer(themes, many=True)
        return Response(serializer.data)


class ThemeView(APIView):
    """Print Theme"""

    def get(self, request, pk):
        theme = Theme.objects.get(id=pk)
        serializer = ThemeSerializer(theme)
        return Response(serializer.data)