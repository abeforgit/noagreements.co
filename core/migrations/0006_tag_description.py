# Generated by Django 3.1.1 on 2020-10-04 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201004_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.CharField(default='description', max_length=2000),
            preserve_default=False,
        ),
    ]
