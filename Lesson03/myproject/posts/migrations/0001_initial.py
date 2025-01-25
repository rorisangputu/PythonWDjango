# Generated by Django 4.2.18 on 2025-01-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Posts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=75)),
                ("body", models.TextField()),
                ("slug", models.SlugField()),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
