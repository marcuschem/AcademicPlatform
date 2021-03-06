# Generated by Django 4.0.5 on 2022-06-12 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0010_alter_module_course'),
        ('practice', '0012_alter_contents_options_contents_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='practice.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='lectures.module'),
        ),
    ]
