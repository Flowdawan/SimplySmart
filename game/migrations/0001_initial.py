# Generated by Django 4.0 on 2021-12-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_1', models.CharField(default='', max_length=600)),
                ('answer_1_right_one', models.CharField(default='', max_length=400)),
                ('answer_2', models.CharField(default='', max_length=400)),
                ('answer_3', models.CharField(default='', max_length=400)),
                ('answer_4', models.CharField(default='', max_length=400)),
            ],
        ),
    ]
