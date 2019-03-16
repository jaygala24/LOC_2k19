# Generated by Django 2.1.7 on 2019-03-16 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='date_time',
            new_name='timestamp',
        ),
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.Donor'),
        ),
    ]