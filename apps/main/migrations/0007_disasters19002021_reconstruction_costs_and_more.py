# Generated by Django 4.2.2 on 2023-06-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_alter_disasters19002021_admin2_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="disasters19002021",
            name="reconstruction_costs",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="disasters19702021",
            name="reconstruction_costs",
            field=models.IntegerField(default=0),
        ),
    ]