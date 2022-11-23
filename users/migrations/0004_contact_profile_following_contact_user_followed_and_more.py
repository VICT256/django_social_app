# Generated by Django 4.0.2 on 2022-05-06 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', through='users.Contact', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_followed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_followed_set', to='users.profile'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_follower_set', to='users.profile'),
        ),
    ]