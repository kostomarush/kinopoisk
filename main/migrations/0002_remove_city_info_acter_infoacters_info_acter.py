# Generated by Django 4.2.13 on 2024-05-14 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='info_acter',
        ),
        migrations.AddField(
            model_name='infoacters',
            name='info_acter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.city'),
        ),
    ]
