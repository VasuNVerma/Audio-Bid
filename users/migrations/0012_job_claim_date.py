# Generated by Django 4.1.2 on 2022-11-13 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_job_url2transcript"),
    ]

    operations = [
        migrations.AddField(
            model_name="job", name="claim_date", field=models.DateTimeField(null=True),
        ),
    ]
