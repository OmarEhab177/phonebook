# Generated by Django 3.2 on 2023-01-16 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='contacts.contact'),
        ),
        migrations.AlterUniqueTogether(
            name='phonenumber',
            unique_together={('number', 'contact')},
        ),
    ]
