# Generated by Django 2.2.12 on 2022-06-11 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=240)),
                ('amount', models.FloatField()),
                ('to_account', models.CharField(max_length=240)),
                ('from_account', models.CharField(max_length=240)),
                ('direction', models.CharField(max_length=8)),
            ],
        ),
    ]
