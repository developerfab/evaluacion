# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadrado',
            name='workspace',
            field=models.ForeignKey(blank=True, to='evaluacion.WorkSpace', null=True),
        ),
        migrations.AlterField(
            model_name='hexagono',
            name='workspace',
            field=models.ForeignKey(blank=True, to='evaluacion.WorkSpace', null=True),
        ),
        migrations.AlterField(
            model_name='triangulo',
            name='workspace',
            field=models.ForeignKey(blank=True, to='evaluacion.WorkSpace', null=True),
        ),
    ]
