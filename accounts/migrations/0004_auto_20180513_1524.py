# Generated by Django 2.0.3 on 2018-05-13 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_estudante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='ano_ingresso',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='matricula',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='nome_mae',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='serie',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
