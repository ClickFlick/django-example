# Generated by Django 3.0.5 on 2020-05-02 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200501_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
                ('email', models.EmailField(default='', max_length=220, unique=True)),
                ('subject', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=250)),
                ('contacted', models.BooleanField(default=False, verbose_name='Contacted')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(default='Order', max_length=200),
        ),
    ]