# Generated by Django 5.0.2 on 2024-02-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0045_alter_doctor_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/'),
        ),
    ]
