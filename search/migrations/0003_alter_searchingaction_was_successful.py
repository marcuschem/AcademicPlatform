# Generated by Django 4.0.5 on 2022-06-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_alter_searchingaction_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchingaction',
            name='was_successful',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
