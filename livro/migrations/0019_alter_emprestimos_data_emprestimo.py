# Generated by Django 4.1.2 on 2022-10-20 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livro", "0018_auto_20211028_1634"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emprestimos",
            name="data_emprestimo",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 20, 18, 33, 22, 360430)
            ),
        ),
    ]
