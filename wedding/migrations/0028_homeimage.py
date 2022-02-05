# Generated by Django 4.0.1 on 2022-02-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0027_weddingpartymember_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videomobile', models.FileField(blank=True, null=True, upload_to='img')),
                ('videodesktop', models.FileField(blank=True, null=True, upload_to='img')),
            ],
        ),
    ]