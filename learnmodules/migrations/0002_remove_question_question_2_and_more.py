# Generated by Django 4.0 on 2021-12-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnmodules', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_4',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='answer_4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_1',
            field=models.CharField(default='', max_length=200),
        ),
    ]
