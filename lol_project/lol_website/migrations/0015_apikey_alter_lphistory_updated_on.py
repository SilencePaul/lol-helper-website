# Generated by Django 5.0 on 2024-04-15 21:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol_website', '0014_rename_update_on_lphistory_updated_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='lphistory',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
