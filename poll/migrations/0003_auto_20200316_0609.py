# Generated by Django 3.0.4 on 2020-03-16 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20200315_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='availability',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Date'),
        ),
    ]