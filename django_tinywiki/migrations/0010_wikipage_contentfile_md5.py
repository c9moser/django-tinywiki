# Generated by Django 4.2.7 on 2024-02-10 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_tinywiki', '0009_alter_wikiimage_alt_alter_wikiimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipage',
            name='contentfile_md5',
            field=models.CharField(default=None, max_length=32, null=True),
        ),
    ]
