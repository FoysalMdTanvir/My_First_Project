# Generated by Django 2.2.5 on 2020-10-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musician',
            old_name='instrumemt',
            new_name='instrument',
        ),
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Worst'), (2, 'Bad'), (3, 'Not Bad'), (4, 'Good'), (5, 'Excelent')]),
        ),
    ]
