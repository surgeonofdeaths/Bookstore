# Generated by Django 4.1.5 on 2023-01-20 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
