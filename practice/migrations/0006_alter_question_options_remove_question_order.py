# Generated by Django 4.0.5 on 2022-06-10 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_alter_question_options_question_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RemoveField(
            model_name='question',
            name='order',
        ),
    ]