# Generated by Django 4.2.5 on 2023-10-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_last_login_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predict_details',
            fields=[
                ('predict_id', models.AutoField(primary_key=True, serialize=False)),
                ('Field_1', models.CharField(max_length=60, null=True)),
                ('Field_2', models.CharField(max_length=60, null=True)),
                ('Field_3', models.CharField(max_length=60, null=True)),
                ('Field_4', models.CharField(max_length=60, null=True)),
                ('Field_5', models.CharField(max_length=60, null=True)),
                ('Field_6', models.CharField(max_length=60, null=True)),
                ('Field_7', models.CharField(max_length=60, null=True)),
                ('Field_8', models.CharField(max_length=60, null=True)),
                ('Field_9', models.CharField(max_length=60, null=True)),
                ('Field_10', models.CharField(max_length=60, null=True)),
            ],
            options={
                'db_table': 'predict_detail',
            },
        ),
    ]
