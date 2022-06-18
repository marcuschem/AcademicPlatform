# Generated by Django 4.0.5 on 2022-06-09 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('lectures', '0006_answer_alter_file_options_alter_image_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('text', 'video', 'image', 'file')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Bank',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
