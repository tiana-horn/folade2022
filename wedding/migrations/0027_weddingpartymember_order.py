# Generated by Django 4.0.1 on 2022-02-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0026_remove_invitation_extra_guests_guest_aso_ebi_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weddingpartymember',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
