# Generated by Django 4.2 on 2023-05-14 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aimals', '0003_alter_animals_date_of_death_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lineage',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('offspring_names', models.CharField(max_length=255)),
                ('parent_names', models.CharField(max_length=255)),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aimals.animals')),
            ],
        ),
    ]
