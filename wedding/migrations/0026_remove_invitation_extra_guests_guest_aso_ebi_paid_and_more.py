# Generated by Django 4.0.1 on 2022-01-29 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0025_guest_aso_ebi_guest_hotel_accomodations_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='extra_guests',
        ),
        migrations.AddField(
            model_name='guest',
            name='aso_ebi_paid',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='guest',
            name='aso_ebi',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='guest',
            name='hotel_accomodations',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.CreateModel(
            name='Plus_One',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('accompanying', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wedding.invitation')),
            ],
        ),
    ]
