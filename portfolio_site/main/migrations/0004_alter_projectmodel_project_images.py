# Generated by Django 4.2.2 on 2023-07-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_projectmodel_delete_testmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='project_images',
            field=models.ImageField(default='Project Images', upload_to='static/images'),
        ),
    ]