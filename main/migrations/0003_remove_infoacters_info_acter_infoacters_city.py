# Generated by Django 4.2.13 on 2024-05-14 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_city_info_acter_infoacters_info_acter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoacters',
            name='info_acter',
        ),
        migrations.AddField(
            model_name='infoacters',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.city'),
        ),
    ]
