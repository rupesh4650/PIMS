# Generated by Django 5.0.1 on 2024-02-02 10:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0024_remove_hospitalstaffadmin_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HospitalStaffAdmin',
            new_name='Staff',
        ),
    ]
