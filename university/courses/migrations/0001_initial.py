# Generated by Django 5.0.4 on 2024-04-23 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('degree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the course name', max_length=50, unique=True, verbose_name='Course Name')),
                ('credits', models.IntegerField(help_text="Enter course's credits", verbose_name='Total Credits')),
                ('description', models.TextField(help_text='Enter the course description', max_length=500, verbose_name='Course Description')),
                ('degree_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='degree.degrees')),
            ],
            options={
                'db_table': 'courses',
                'ordering': ['name'],
            },
        ),
    ]
