# Generated by Django 3.1.13 on 2022-04-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_emaildata_twitterdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaildata',
            name='site',
            field=models.TextField(blank=True, null=True),
        ),
    ]