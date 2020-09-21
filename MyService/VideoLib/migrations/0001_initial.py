# Generated by Django 3.0.8 on 2020-09-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_no', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('mobile_no', models.CharField(max_length=255)),
                ('avatar', models.ImageField(upload_to='avatars/%Y/%m/%d/')),
                ('sex', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'video_lib_user',
            },
        ),
    ]
