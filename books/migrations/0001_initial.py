# Generated by Django 4.2.6 on 2023-10-15 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
