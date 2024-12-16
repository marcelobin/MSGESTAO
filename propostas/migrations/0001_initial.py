# Generated by Django 5.1.4 on 2024-12-15 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('financeiras', '0001_initial'),
        ('lojas', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id_veiculo', models.AutoField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=100)),
                ('placa', models.CharField(max_length=10)),
                ('renavam', models.CharField(max_length=20)),
                ('chassi', models.CharField(max_length=30)),
                ('valor_veiculo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propostas.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id_proposta', models.AutoField(primary_key=True, serialize=False)),
                ('nro_proposta', models.CharField(max_length=50, unique=True)),
                ('valor_financiado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prazo', models.PositiveIntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('contato_comercial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario')),
                ('financeira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiras.financeira')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojas.loja')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lojas.vendedor')),
                ('veiculo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='propostas.veiculo')),
            ],
        ),
    ]