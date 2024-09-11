# Generated by Django 4.2.15 on 2024-09-11 10:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0027_attributeoption_code_attributeoptiongroup_code_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="priority",
            field=models.SmallIntegerField(
                db_index=True,
                default=0,
                help_text="The highest priority products are shown first, use -1 to make products less important",
                validators=[django.core.validators.MinValueValidator(-1)],
                verbose_name="Priority",
            ),
        ),
    ]
