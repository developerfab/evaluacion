# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuadrado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numLados', models.IntegerField()),
                ('lado', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hexagono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numLados', models.IntegerField()),
                ('radio', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Triangulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numLados', models.IntegerField()),
                ('base', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('hipotenusa', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkSpace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('limiteFiguras', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='triangulo',
            name='workspace',
            field=models.ForeignKey(to='evaluacion.WorkSpace'),
        ),
        migrations.AddField(
            model_name='hexagono',
            name='workspace',
            field=models.ForeignKey(to='evaluacion.WorkSpace'),
        ),
        migrations.AddField(
            model_name='cuadrado',
            name='workspace',
            field=models.ForeignKey(to='evaluacion.WorkSpace'),
        ),
    ]
