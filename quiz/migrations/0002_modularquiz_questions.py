# Generated by Django 4.0.5 on 2022-06-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0014_alter_contents_order_alter_question_order'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modularquiz',
            name='questions',
            field=models.ManyToManyField(blank=True, related_name='questions', to='practice.question'),
        ),
    ]