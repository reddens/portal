# Generated by Django 3.2.5 on 2021-10-02 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prospects', '0002_auto_20211002_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='guradian_lga',
            new_name='guardian_lga',
        ),
    ]
