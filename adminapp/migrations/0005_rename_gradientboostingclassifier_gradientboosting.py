# Generated by Django 4.2.5 on 2023-10-09 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_gradientboostingclassifier'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GradientBoostingClassifier',
            new_name='GradientBoosting',
        ),
    ]
