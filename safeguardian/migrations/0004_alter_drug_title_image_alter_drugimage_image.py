# Generated by Django 4.2.9 on 2024-02-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safeguardian', '0003_rename_ctgry_id_drug_ctgry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='title_image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='drugimage',
            name='image',
            field=models.URLField(),
        ),
    ]
