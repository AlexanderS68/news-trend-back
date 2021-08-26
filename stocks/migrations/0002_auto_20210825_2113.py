# Generated by Django 3.2.6 on 2021-08-25 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='bidPrice',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='closePrice',
            field=models.CharField(blank=True, default=100, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='divAmount',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='divDate',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='mark',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='markPercentChangeInDouble',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='openPrice',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='peRatio',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='totalVolume',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='volatility',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]