# Generated by Django 4.1.5 on 2023-03-05 11:16

from django.db import migrations, models
import fotos.models


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='image',
            field=models.ImageField(upload_to=fotos.models.PathAndRename('fotos/')),
        ),
    ]
