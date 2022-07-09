# Generated by Django 4.0.5 on 2022-07-09 04:52

import app_catalog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
            ],
            options={
                'verbose_name': 'manufacturer',
                'verbose_name_plural': 'manufacturers',
                'db_table': 'manufacturer',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
            ],
            options={
                'verbose_name': 'parameter',
                'verbose_name_plural': 'parameters',
                'db_table': 'parameter',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('short_description', models.CharField(max_length=400, verbose_name='short description')),
                ('description', models.TextField(max_length=2000, verbose_name='description')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('created_at', models.TimeField(auto_now_add=True, verbose_name='creation date')),
                ('edited_at', models.TimeField(auto_now=True, verbose_name='edit date')),
                ('is_limited', models.BooleanField(default=False, verbose_name='is limited')),
                ('is_available', models.BooleanField(default=True, verbose_name='is available')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='app_catalog.category', verbose_name='category')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='app_catalog.manufacturer', verbose_name='manufacturer')),
                ('tags', models.ManyToManyField(related_name='item', to='app_catalog.tag', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'db_table': 'item',
                'permissions': (('change_limited', 'Can change if item is limited'), ('change_available', 'Can change if item is available')),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=app_catalog.models.user_directory_path, verbose_name='image')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='app_catalog.item', verbose_name='item')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'db_table': 'image',
            },
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('name', models.CharField(blank=True, max_length=32, verbose_name='name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('is_verified', models.BooleanField(default=True, verbose_name='is verified')),
                ('created_at', models.TimeField(auto_now_add=True, verbose_name='creation date')),
                ('edited_at', models.TimeField(auto_now=True, verbose_name='edit date')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentary', to='app_catalog.item', verbose_name='item')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentary', to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'verbose_name': 'commentary',
                'verbose_name_plural': 'commentaries',
                'db_table': 'commentary',
                'permissions': (('change_verified', 'Can change if commentary is verified'),),
            },
        ),
        migrations.CreateModel(
            name='ParameterValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=128, verbose_name='value')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_catalog.item', verbose_name='item')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_catalog.parameter', verbose_name='item')),
            ],
            options={
                'verbose_name': 'parameter_value',
                'verbose_name_plural': 'parameter_values',
                'db_table': 'parameter_value',
                'unique_together': {('item', 'parameter')},
            },
        ),
    ]
