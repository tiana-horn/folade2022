# Generated by Django 4.0.1 on 2022-01-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0020_weddingpartycarouselimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='weddingpartymember',
            name='bridal_side',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='weddingpartymember',
            name='groom_side',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='storytext',
            name='p1_bold',
            field=models.CharField(max_length=777),
        ),
        migrations.AlterField(
            model_name='storytext',
            name='p1_part1',
            field=models.TextField(max_length=77777),
        ),
        migrations.AlterField(
            model_name='storytext',
            name='p1_part2',
            field=models.TextField(max_length=77777),
        ),
        migrations.AlterField(
            model_name='storytext',
            name='p2_bold',
            field=models.CharField(max_length=777),
        ),
        migrations.AlterField(
            model_name='storytext',
            name='p2_part1',
            field=models.TextField(max_length=77777),
        ),
        migrations.AlterField(
            model_name='storytext',
            name='p2_part2',
            field=models.TextField(max_length=77777),
        ),
    ]
