# Generated by Django 5.0.6 on 2024-06-26 00:20

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_kater_remove_participationapplication_course_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='zakaz',
            name='data',
            field=models.DateTimeField(default=1, verbose_name='Дата заявки '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kater',
            name='opisanie',
            field=models.CharField(max_length=1000, verbose_name='Описание катера'),
        ),
        migrations.AlterField(
            model_name='remont',
            name='data',
            field=models.DateField(verbose_name='Дата ремонта'),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона долже быть в формате: '+79998887799'. До 15 символов длиной.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Номер телефона'),
        ),
        migrations.CreateModel(
            name='Zapros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона долже быть в формате: '+79998887799'. До 15 символов длиной.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Номер телефона')),
                ('title', models.CharField(max_length=255, verbose_name='О себе')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Kandidat', to=settings.AUTH_USER_MODEL, verbose_name='Кандидат')),
            ],
            options={
                'verbose_name': 'Кандидат',
                'verbose_name_plural': 'Кандидаты',
            },
        ),
    ]
