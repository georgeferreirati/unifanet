# Generated by Django 2.0.3 on 2018-05-13 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180513_1524'),
        ('turmas', '0005_nota'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='estudantes',
            field=models.ManyToManyField(to='accounts.Estudante'),
        ),
    ]