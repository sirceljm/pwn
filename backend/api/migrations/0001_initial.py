# Generated by Django 5.0.7 on 2024-08-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('wallet_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('nfts', models.JSONField(null=True)),
                ('tokens', models.JSONField(null=True)),
                ('transactions', models.JSONField(null=True)),
            ],
        ),
    ]
