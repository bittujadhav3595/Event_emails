# Generated by Django 4.2.4 on 2023-08-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('Birthday', 'Birthday'), ('Work Anniversary', 'Work Anniversary')], max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10)),
                ('event_type', models.CharField(choices=[('Birthday', 'Birthday'), ('Work Anniversary', 'Work Anniversary')], max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
