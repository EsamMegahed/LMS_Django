# Generated by Django 5.0.6 on 2024-06-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(default=1, upload_to='courses_images'),
            preserve_default=False,
        ),
    ]