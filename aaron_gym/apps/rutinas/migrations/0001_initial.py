# Generated by Django 4.1.7 on 2023-03-15 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cuerpo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField(null=True)),
                ('file', models.FileField(upload_to='rutinas')),
                ('img', models.ImageField(null=True, upload_to='videos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutinas.categoria')),
                ('cuerpo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rutinas.cuerpo')),
            ],
        ),
    ]