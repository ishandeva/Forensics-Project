# Generated by Django 3.0 on 2020-01-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.BigIntegerField()),
                ('date', models.DateField()),
                ('details', models.CharField(max_length=500)),
                ('withdrawal_amt', models.FloatField(blank=True, null=True)),
                ('deposit_amt', models.FloatField(blank=True, null=True)),
                ('balance', models.FloatField()),
            ],
        ),
    ]