# Generated by Django 4.0.5 on 2022-06-07 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_alter_course_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'Archivo'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Imagen'},
        ),
        migrations.AlterModelOptions(
            name='text',
            options={'verbose_name': 'Texto'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Video'},
        ),
    ]