# Generated by Django 4.2.2 on 2023-06-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disasters19002021",
            name="adm_level",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="disasters19702021",
            name="adm_level",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
