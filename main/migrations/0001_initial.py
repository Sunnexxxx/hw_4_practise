# Generated by Django 4.2.7 on 2023-11-10 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Json',
            fields=[
                ('userId', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField()),
            ],
        ),
    ]