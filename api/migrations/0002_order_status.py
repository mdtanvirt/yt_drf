# Generated by Django 5.2 on 2025-05-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confiremed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
    ]
