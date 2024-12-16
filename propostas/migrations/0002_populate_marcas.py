from django.db import migrations

def populate_marcas(apps, schema_editor):
    Marca = apps.get_model('propostas', 'Marca')
    marcas = [
        'Chevrolet', 'Fiat', 'Ford', 'Volkswagen', 'Toyota', 'Honda', 
        'Hyundai', 'Renault', 'Nissan', 'Jeep', 'Citroën', 'Peugeot', 
        'Mitsubishi', 'Kia', 'BMW', 'Mercedes-Benz', 'Audi', 'Volvo', 
        'Land Rover', 'Jaguar', 'Chery', 'Suzuki', 'Subaru', 'Porsche', 
        'Lexus', 'Ram', 'Mini', 'Ferrari', 'Maserati', 'Bentley', 
        'Rolls-Royce', 'Lamborghini', 'Aston Martin', 'Bugatti'
    ]
    for marca in marcas:
        Marca.objects.create(nome=marca)

class Migration(migrations.Migration):

    dependencies = [
        ('propostas', '0001_initial'),  # Substitua pelo nome da migração anterior
    ]

    operations = [
        migrations.RunPython(populate_marcas),
    ]