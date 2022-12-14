# Generated by Django 4.1.2 on 2022-12-02 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.BigIntegerField(default='-1')),
                ('creator_id', models.CharField(default='0', max_length=100)),
                ('worker_id', models.CharField(default='0', max_length=100)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('review', models.TextField(blank=True, max_length=500)),
                ('rating', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=10)),
                ('time_zone', models.CharField(max_length=500)),
                ('native_auth', models.BooleanField(default=False)),
                ('rating', models.FloatField(default=0.0)),
                ('number_of_ratings', models.IntegerField(default='0')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('limit_price', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('cron_date', models.DateTimeField(null=True)),
                ('claim_date', models.DateTimeField(null=True)),
                ('description', models.TextField()),
                ('url2audio', models.TextField()),
                ('url2Transcript', models.TextField(null=True)),
                ('worker_id', models.CharField(default='0', max_length=100)),
                ('content', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'AVAILABLE'), (1, 'INPROGRESS'), (2, 'COMPLETED'), (3, 'INREVIEW')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.job')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
