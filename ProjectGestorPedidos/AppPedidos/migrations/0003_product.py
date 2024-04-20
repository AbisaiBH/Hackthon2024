# Generated by Django 5.0.4 on 2024-04-20 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPedidos', '0002_remove_form_user_date_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('embedding', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
