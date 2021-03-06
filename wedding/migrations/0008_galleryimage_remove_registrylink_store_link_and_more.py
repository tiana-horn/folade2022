# Generated by Django 4.0.1 on 2022-01-20 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0007_rename_zola_link_registrylink_zolalink'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='img')),
                ('image_alt_text', models.CharField(max_length=111)),
            ],
        ),
        migrations.RemoveField(
            model_name='registrylink',
            name='store_link',
        ),
        migrations.RemoveField(
            model_name='registrylink',
            name='store_logo',
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='registrylink',
            name='zola_data_registry_key',
            field=models.CharField(blank=True, max_length=222),
        ),
        migrations.AlterField(
            model_name='storytext',
            name='image1',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='storytext',
            name='image2',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='weddingpartymember',
            name='description',
            field=models.TextField(blank=True, max_length=777),
        ),
        migrations.AlterField(
            model_name='weddingpartymember',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
