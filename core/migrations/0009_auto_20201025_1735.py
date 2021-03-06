# Generated by Django 3.1.1 on 2020-10-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20201004_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='artist_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='bandcamp_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='spotify_url',
            field=models.URLField(blank=True),
        ),
    ]
