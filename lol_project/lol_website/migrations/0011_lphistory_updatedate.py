# Generated by Django 5.0 on 2024-03-12 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol_website', '0010_lphistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='lphistory',
            name='updateDate',
            field=models.DateTimeField(default=None),
        ),
    ]
