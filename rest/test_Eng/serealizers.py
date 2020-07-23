from rest_framework import serializers
from rest_framework import permissions
from .models import Categories, Theme, Words, Levels


class CaregoriesSerializer(serializers.ModelSerializer):
    """Categories serializer"""
    permission_classes = (permissions.IsAuthenticated,)
    class Meta:
        model = Categories
        fields = ("id", "name", "icon")


class LevelsSerializer(serializers.ModelSerializer):
    """Levels serializer"""
    permission_classes = (permissions.IsAuthenticated,)
    class Meta:
        model = Levels
        fields = ("id", "name", "code")


class WordsSerializer(serializers.ModelSerializer):
    """Words serializer"""
    permission_classes = (permissions.IsAuthenticated,)
    class Meta:
        model = Words
        fields = ("id", "name", "translation", "transcription", "example", "sound")


class ThemesSerializer(serializers.ModelSerializer):
    """Themes serializer"""
    permission_classes = (permissions.IsAuthenticated,)
    class Meta:
        model = Theme
        exclude = ()




class ThemeSerializer(serializers.ModelSerializer):
    """Theme serializer"""
    permission_classes = (permissions.IsAuthenticated,)
    words_to_theme = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    class Meta:
        model = Theme
        exclude = ()
