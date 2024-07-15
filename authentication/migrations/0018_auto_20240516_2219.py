# Generated by Django 3.2.1 on 2024-05-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_alter_bloodbank_options_alter_userprofile_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbank',
            name='bloodbankaccreditations',
            field=models.CharField(max_length=2000, verbose_name='Accreditaions'),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='bloodbanklink',
            field=models.CharField(max_length=5000, verbose_name='Website Link'),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='bloodbanklocation',
            field=models.CharField(max_length=5000, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=5000),
        ),
    ]
