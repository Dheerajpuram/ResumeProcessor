# Generated by Django 5.1.4 on 2025-01-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume_app", "0002_candidate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="email",
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
