# Generated by Django 2.1.5 on 2021-02-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
