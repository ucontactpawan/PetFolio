# Generated by Django 4.2.2 on 2023-06-24 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 9, 10, 46, 824017, tzinfo=datetime.timezone.utc)),
        ),
    ]
