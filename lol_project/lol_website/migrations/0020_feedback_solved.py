# Generated by Django 5.0 on 2024-04-30 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol_website', '0019_feedback_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='solved',
            field=models.BooleanField(default=False),
        ),
    ]
