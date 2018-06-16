# Generated by Django 2.0.3 on 2018-05-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180513_1524'),
        ('turmas', '0008_presenca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presenca',
            name='aula',
        ),
        migrations.RemoveField(
            model_name='presenca',
            name='estudante',
        ),
        migrations.AddField(
            model_name='aula',
            name='presenca',
            field=models.ManyToManyField(to='accounts.Estudante'),
        ),
        migrations.DeleteModel(
            name='Presenca',
        ),
    ]
