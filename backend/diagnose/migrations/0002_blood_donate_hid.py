# Generated by Django 3.2.5 on 2021-10-09 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood_donate',
            name='hid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diagnose.blood_bank'),
        ),
    ]
