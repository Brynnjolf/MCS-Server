# Generated by Django 2.2.4 on 2019-09-02 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190806_0340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyprofile',
            old_name='overviews',
            new_name='overview',
        ),
    ]