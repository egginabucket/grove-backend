# Generated by Django 4.1.2 on 2022-11-24 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("translator", "0002_alter_googlelanguage_display_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="googlelanguage",
            old_name="language_tag",
            new_name="lang",
        ),
    ]
