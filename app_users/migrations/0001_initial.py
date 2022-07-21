# Generated by Django 4.0.5 on 2022-07-14 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_catalog', '0002_category_icon_id_category_sort_index_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMedia',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_catalog.media')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_media', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user_media',
                'verbose_name_plural': 'user_medias',
                'db_table': 'user_media',
            },
            bases=('app_catalog.media',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=50, verbose_name='middle name')),
                ('phone_number', models.CharField(max_length=10, verbose_name='phone number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='edit date')),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile', to='app_users.usermedia', verbose_name='avatar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'profile',
            },
        ),
    ]