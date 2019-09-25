# Generated by Django 2.2.5 on 2019-09-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_type',
            field=models.CharField(choices=[('super_admin', 'super admin'), ('admin', 'admin'), ('moderator', 'moderator'), ('user', 'user'), ('guest', 'guest')], max_length=20, unique=True),
        ),
    ]