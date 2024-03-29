# Generated by Django 4.0.6 on 2022-07-21 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewWord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=20, unique=True)),
                ('explain', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('likeCnt', models.IntegerField(default=0)),
                ('create_user_id', models.ForeignKey(db_column='create_user_id', on_delete=django.db.models.deletion.CASCADE, related_name='newword', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='NewWord_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Newword_id', models.ForeignKey(db_column='post_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.newword')),
                ('user_id', models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'db_table': 'NewWord_user',
            },
        ),
        migrations.AddField(
            model_name='newword',
            name='like_user_ids',
            field=models.ManyToManyField(blank=True, related_name='likeword', through='main.NewWord_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
