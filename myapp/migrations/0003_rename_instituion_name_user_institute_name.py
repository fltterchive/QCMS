# Generated by Django 4.1.7 on 2023-03-27 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_full_name_user_instituion_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='instituion_name',
            new_name='institute_name',
        ),
    ]
