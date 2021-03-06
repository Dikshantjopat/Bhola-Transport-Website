# Generated by Django 2.0.7 on 2018-08-20 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=250)),
                ('destination', models.CharField(max_length=250)),
                ('material', models.CharField(choices=[('Cement', 'Cement'), ('House Hold Goods', 'House Hold Goods'), ('Building Materials', 'Building Materials'), ('Chemicals', 'Chemicals'), ('Coal And Ash', 'Coal And Ash'), ('Container', 'Container'), ('Cotton seed', 'Cotton seed'), ('Fertilizers', 'Fertilizers'), ('Fruits And Vegetables', 'Fruits And Vegetables'), ('Furniture And Wood Products', 'Furniture And Wood Products'), ('Industrial Equipments', 'Industrial Equipments'), ('Iron sheets or bars or scraps', 'Iron sheets or bars or scraps'), ('Medicals', 'Medicals'), ('Metals', 'Metals'), ('Mill Jute Oil', 'Mill Jute Oil'), ('Others', 'Others'), ('Packed Food', 'Packed Food'), ('Plastic Pipes or other products', 'Plastic Pipes or other products')], default='black', max_length=50)),
                ('truck_type', models.CharField(choices=[('loader', 'Loader'), ('truck', 'Truck')], default='black', max_length=50)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]
