# Generated by Django 3.2 on 2022-03-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='sem',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='usn',
            new_name='regno',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='contact',
            name='year',
            field=models.CharField(default='', max_length=50),
        ),
    ]
