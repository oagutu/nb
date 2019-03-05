# Generated by Django 2.1.7 on 2019-03-05 09:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.UUIDField(null=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2019, 3, 5, 9, 3, 40, 544169, tzinfo=utc))),
                ('edited_by', models.UUIDField(null=True)),
                ('edited_on', models.DateTimeField(null=True)),
                ('deleted_by', models.UUIDField(null=True)),
                ('deleted_on', models.DateTimeField(null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
                ('domain', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
