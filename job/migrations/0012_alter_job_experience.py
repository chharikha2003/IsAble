# Generated by Django 5.0 on 2024-01-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_alter_job_city_alter_job_disability_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(blank=True, choices=[('Entry Level', 'Entry Level'), ('1 Year', '1 Year'), ('2 Years', '2 Years'), ('3 Years', '3 Years'), ('4 Years', '4 Years'), ('5+ Years', '5+ Years')], max_length=50, null=True),
        ),
    ]
