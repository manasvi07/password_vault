# Generated by Django 3.2.10 on 2022-03-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0005_alter_vault_encrypted_remainder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vault',
            name='encrypted_remainder',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]