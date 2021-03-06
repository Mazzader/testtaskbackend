# Generated by Django 3.0.8 on 2020-07-22 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='categories')),
                ('icon', models.ImageField(upload_to='', verbose_name='icon')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='levels')),
                ('code', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=2, verbose_name='level code')),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('photo', models.ImageField(upload_to='', verbose_name='photo')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_to_theme', to='test_Eng.Categories', verbose_name='theme_categories_verbose')),
                ('levels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels_to_theme', to='test_Eng.Levels', verbose_name='theme_levels_verbose')),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
            },
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('translation', models.TextField(verbose_name='translation')),
                ('transcription', models.TextField(verbose_name='transcription')),
                ('example', models.TextField(verbose_name='example')),
                ('sound', models.FileField(upload_to='', verbose_name='sound')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words_to_theme', to='test_Eng.Theme', verbose_name='words_theme_verbose')),
            ],
            options={
                'verbose_name': 'Word',
                'verbose_name_plural': 'Words',
            },
        ),
    ]
