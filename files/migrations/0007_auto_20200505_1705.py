# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-05 17:05


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0006_theme_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='release_notes_markup_type',
            field=models.CharField(choices=[('', '--'), ('html', 'HTML'), ('plain', 'Plain'), ('markdown', 'Markdown'), ('restructuredtext', 'Restructured Text')], default='markdown', max_length=30),
        ),
    ]
