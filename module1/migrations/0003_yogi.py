# Generated by Django 4.2.6 on 2024-02-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yogi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('pass1', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Yogi',
            },
        ),
    ]
