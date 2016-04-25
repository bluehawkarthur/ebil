# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0010_proveedorescampos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientecampos',
            old_name='codigo_requerido',
            new_name='fecha2_requerido',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='codigo_usar',
            new_name='fecha2_usar',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='nit_requerido',
            new_name='fecha_requerido',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='nit_usar',
            new_name='fecha_usar',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='codigo_caractr',
            new_name='telefono1_caractr',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='razonsocal_requerido',
            new_name='telefono1_requerido',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='codigo_tipo',
            new_name='telefono1_tipo',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='razonsocal_usar',
            new_name='telefono1_usar',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='nit_caractr',
            new_name='telefono2_caractr',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='telefonos_requerido',
            new_name='telefono2_requerido',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='nit_tipo',
            new_name='telefono2_tipo',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='telefonos_usar',
            new_name='telefono2_usar',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='razonsocal_caractr',
            new_name='telefono3_caractr',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='razonsocal_tipo',
            new_name='telefono3_tipo',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='telefonos_caractr',
            new_name='texto2_caractr',
        ),
        migrations.RenameField(
            model_name='clientecampos',
            old_name='telefonos_tipo',
            new_name='texto2_tipo',
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='telefono3_requerido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='telefono3_usar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='texto2_requerido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='texto2_usar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='texto_caractr',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='texto_requerido',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='texto_tipo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientecampos',
            name='texto_usar',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientecampos',
            name='empresa',
            field=models.ForeignKey(to='users.Personajuridica', null=True),
        ),
    ]
