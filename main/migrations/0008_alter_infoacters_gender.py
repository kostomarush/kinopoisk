# Generated by Django 4.2.13 on 2024-05-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_kinofilms_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoacters',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], max_length=1),
        ),
    ]
