# Generated by Django 4.0.5 on 2022-06-06 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('agent_username', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('provider', models.CharField(choices=[('NZ BEST', 'NZ Best Tour Company'), ('NZ First', 'New Zealand First'), ('Little Black Bus', 'Little Black Individual Tours')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('available', models.BooleanField()),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.agent')),
                ('duration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.duration')),
            ],
            options={
                'permissions': (('can_change_availability', 'Set tour as available'),),
            },
        ),
    ]
