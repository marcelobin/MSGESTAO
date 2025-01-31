# Generated by Django 5.1.4 on 2024-12-15 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filiais', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id_loja', models.AutoField(primary_key=True, serialize=False)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('razao_social', models.CharField(max_length=200)),
                ('nome_fantasia', models.CharField(max_length=200)),
                ('data_constituicao', models.DateField()),
                ('cep', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=200)),
                ('nro', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contato_comercial', models.ForeignKey(blank=True, limit_choices_to={'funcao__in': ['CCE', 'CCI', 'ADMIN']}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario')),
                ('filial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filiais.filial')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id_socio', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField()),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socios', to='lojas.loja')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id_vendedor', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('chave_pix', models.CharField(blank=True, max_length=100, null=True)),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendedores', to='lojas.loja')),
            ],
        ),
    ]
