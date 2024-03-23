# Generated by Django 4.2.5 on 2023-10-06 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADA_ALGO',
            fields=[
                ('ADA_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'ADA_algo',
            },
        ),
        migrations.CreateModel(
            name='ANM_ALGO',
            fields=[
                ('ANM_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'ANM_algo',
            },
        ),
        migrations.CreateModel(
            name='ANN_ALGO',
            fields=[
                ('ANN_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'ANN_algo',
            },
        ),
        migrations.CreateModel(
            name='DATASET',
            fields=[
                ('DS_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Age', models.IntegerField()),
                ('Glucose', models.IntegerField()),
                ('BloodPressure', models.IntegerField()),
                ('SkinThickness', models.IntegerField()),
                ('Insulin', models.IntegerField()),
                ('BMI', models.IntegerField()),
                ('DiabetesPedigreeFunction', models.IntegerField()),
                ('Pregnancies', models.IntegerField()),
            ],
            options={
                'db_table': 'Dataset',
            },
        ),
        migrations.CreateModel(
            name='DECISSION_ALGO',
            fields=[
                ('DECISSION_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'DECISSION_algo',
            },
        ),
        migrations.CreateModel(
            name='DT_ALGO',
            fields=[
                ('DT_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'DT_algo',
            },
        ),
        migrations.CreateModel(
            name='KNN_ALGO',
            fields=[
                ('KNN_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'KNN_algo',
            },
        ),
        migrations.CreateModel(
            name='SXM_ALGO',
            fields=[
                ('SXM_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'SVC_algo',
            },
        ),
        migrations.CreateModel(
            name='Upload_dataset_model',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('Dataset', models.FileField(null=True, upload_to='')),
                ('File_size', models.CharField(max_length=100)),
                ('Date_Time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'upload_dataset',
            },
        ),
        migrations.CreateModel(
            name='XG_ALGO',
            fields=[
                ('XG_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Accuracy', models.TextField(max_length=100)),
                ('Precession', models.TextField(max_length=100)),
                ('F1_Score', models.TextField(max_length=100)),
                ('Recall', models.TextField(max_length=100)),
                ('Name', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'XG_algo',
            },
        ),
    ]
