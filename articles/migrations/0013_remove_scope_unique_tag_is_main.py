# Generated by Django 5.1.1 on 2024-10-07 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_scope_unique_tag_is_main'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='scope',
            name='unique_tag_is_main',
        ),
    ]
