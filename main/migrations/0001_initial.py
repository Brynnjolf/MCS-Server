# Generated by Django 2.2.3 on 2019-08-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('ticker', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=255)),
            ],
        ),
    ]
