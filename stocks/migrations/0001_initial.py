# Generated by Django 2.2 on 2020-01-04 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='stocks.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity1', models.PositiveIntegerField()),
                ('quantity2', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product1', to='stocks.Product')),
                ('product2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product2', to='stocks.Product')),
                ('site1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site1', to='stocks.Site')),
                ('site2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site2', to='stocks.Site')),
                ('type1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type1', to='stocks.Type')),
                ('type2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type2', to='stocks.Type')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
