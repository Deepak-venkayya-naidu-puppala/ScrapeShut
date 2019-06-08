# Generated by Django 2.1.7 on 2019-06-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_uploadmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadmodel',
            name='choice',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadmodel',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadmodel',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadmodel',
            name='photo',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
