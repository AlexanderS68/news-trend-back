# Generated by Django 3.2.6 on 2021-08-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=100)),
                ('count', models.CharField(blank=True, max_length=100)),
                ('published_at', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
