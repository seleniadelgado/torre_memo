# Generated by Django 2.2.7 on 2019-11-25 11:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0003_auto_20191125_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectionmemos',
            name='id',
        ),
        migrations.AddField(
            model_name='connectionmemos',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
