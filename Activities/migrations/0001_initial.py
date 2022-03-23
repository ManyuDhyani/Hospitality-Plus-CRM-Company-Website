# Generated by Django 4.0.2 on 2022-03-23 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitiesCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Activities Categories',
            },
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('thumbnail', models.ImageField(upload_to='upload/treks')),
                ('recommended', models.BooleanField(blank=True, default=False, null=True)),
                ('altitude', models.CharField(max_length=20)),
                ('duration_days', models.CharField(max_length=20)),
                ('difficulty', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=40)),
                ('distance', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=150)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Activities.activitiescategories')),
            ],
        ),
    ]
