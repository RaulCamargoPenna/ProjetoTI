# Generated by Django 5.1.2 on 2024-10-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallbacksTeste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(default='')),
                ('processado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TokensTeste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
