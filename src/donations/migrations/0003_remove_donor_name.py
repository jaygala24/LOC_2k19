# Generated by Django 2.1.7 on 2019-03-16 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20190316_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='name',
        ),
    ]