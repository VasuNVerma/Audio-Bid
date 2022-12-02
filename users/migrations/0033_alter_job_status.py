# Generated by Django 4.1.2 on 2022-11-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_alter_job_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.IntegerField(choices=[(0, 'AVAILABLE'), (1, 'IN PROGRESS'), (2, 'COMPLETED'), (3, 'IN REVIEW')], default=0),
        ),
    ]
