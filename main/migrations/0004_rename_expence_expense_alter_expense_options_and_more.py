# Generated by Django 4.0.6 on 2022-09-05 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_expense_expence'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expence',
            new_name='Expense',
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['-date_created']},
        ),
    ]
