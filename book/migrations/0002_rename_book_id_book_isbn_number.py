# Generated by Django 4.0.5 on 2022-06-29 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_id',
            new_name='isbn_number',
        ),
    ]
