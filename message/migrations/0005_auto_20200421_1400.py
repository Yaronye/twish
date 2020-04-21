# Generated by Django 3.0.5 on 2020-04-21 14:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20200420_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secret',
            name='id',
        ),
        migrations.AddField(
            model_name='secret',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
