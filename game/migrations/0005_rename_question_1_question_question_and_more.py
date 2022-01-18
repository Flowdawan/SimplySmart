# Generated by Django 4.0 on 2022-01-18 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('game', '0004_alter_questionstat_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_1',
            new_name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='game_mode',
            field=models.CharField(default='elmc', max_length=150),
        ),
        migrations.CreateModel(
            name='PlayerGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(default='', max_length=350)),
                ('question', models.ManyToManyField(to='game.Question')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]