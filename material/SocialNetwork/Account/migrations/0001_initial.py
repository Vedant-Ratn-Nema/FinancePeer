# Generated by Django 2.2.6 on 2019-10-21 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Non binnary')], max_length=1)),
                ('dob', models.DateField()),
                ('about_me', models.CharField(max_length=500)),
                ('collage', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=30)),
                ('workplace', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
