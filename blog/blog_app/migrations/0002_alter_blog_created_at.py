# Generated by Django 3.2.22 on 2023-11-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
