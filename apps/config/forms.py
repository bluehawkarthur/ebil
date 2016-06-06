# -*- coding: utf-8 -*-
from django import forms
from apps.users.models import Personajuridica
from .models import Formatofactura, Sucursal, Actividad, Formatodetalle
from django.forms import modelformset_factory
from django.utils.safestring import mark_safe


class PersonajuridicaForm(forms.Form):
    razon_social = forms.CharField(max_length=100)
    nit = forms.IntegerField()
    direccion = forms.CharField(max_length=100)
    telefono = forms.IntegerField(required=True)
    telefono2 = forms.IntegerField(required=False)
    telefono3 = forms.IntegerField(required=False)
    departamento = forms.CharField(max_length=100)
    municipios = forms.CharField(max_length=100)
    logo = forms.ImageField(required=False, label="Logo")

    def clean_nit(self):
        try:
            Personajuridica.objects.get(nit=self.cleaned_data['nit'])
        except Personajuridica.DoesNotExist:
            return self.cleaned_data['nit']

        raise forms.ValidationError("La empresa con este nit ya existe")


class EmpresaFormedit(forms.ModelForm):
    razon_social = forms.CharField(max_length=100)
    nit = forms.IntegerField()
    direccion = forms.CharField(max_length=100)
    telefono = forms.IntegerField(required=True)
    telefono2 = forms.CharField(required=False)
    telefono3 = forms.CharField(required=False)
    departamento = forms.CharField(max_length=100)
    municipios = forms.CharField(max_length=100)
    logo = forms.ImageField(required=False, label="Logo")

    class Meta:
        model = Personajuridica
        fields = ('razon_social', 'nit', 'direccion', 'telefono', 'departamento', 'municipios', 'logo')


class DatosDosificacionForm(forms.Form):
    nro_conrelativo = forms.IntegerField()
    fecha = forms.DateField(label="Fecha limite de emision")
    nro_autorizacion = forms.IntegerField()
    llave_digital = forms.CharField()
    sucursal = forms.ModelChoiceField(queryset='', empty_label='seleccione')
    actividad = forms.ModelChoiceField(queryset='', empty_label='seleccione')


class FormatofacturaForm(forms.ModelForm):
    formato = forms.CharField(max_length=100)
    impresion = forms.CharField(max_length=100)
    facturacion = forms.CharField(max_length=100)
    tamanio = forms.CharField(max_length=100)
    frases_titulo = forms.CharField(max_length=100)
    frases_subtitulo = forms.CharField(max_length=100)
    frases_pie = forms.CharField(max_length=2100)

    class Meta:
        model = Formatofactura
        fields = ('formato', 'impresion', 'facturacion', 'tamanio', 'frases_titulo', 'frases_subtitulo', 'frases_pie')


class SucursalForm(forms.Form):
    nombre_sucursal = forms.CharField(max_length=100)
    nro_sucursal = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    telefono1 = forms.IntegerField()
    telefono2 = forms.IntegerField(required=False)
    telefono3 = forms.IntegerField(required=False)
    departamento = forms.CharField(max_length=100)
    municipios = forms.CharField(max_length=100)


class ActividadForm(forms.Form):
    actividad = forms.CharField(max_length=100, required=True)


list_of_choices = (
    ('Vacia', 'Vacia'),
    ('Completa', 'Completa'),
    ('Semi-completa', 'Semi-completa'),
)

list_of_facturacion = (
    ('Normal', 'Normal'),
    ('Facturación por terceros', 'Facturación por terceros'),
    ('Conjunta', 'Conjunta'),
)

list_of_frases_titulo = (
    ('Factura', 'Factura'),
    ('Factura por compras', 'Factura por compras'),
    ('Factura Conjunta', 'Factura Conjunta'),
    ('Factura de Alquiler', 'Factura de Alquiler'),
    ('Comercial de Expotacion', 'Comercial de Expotacion'),
    ('En Libre Consignacion', 'En Libre Consignacion'),
    ('Factura Turistica', 'Factura Turistica'),
    ('Factura Artistas Nacionales', 'Factura Artistas Nacionales'),
)

list_of_frases_subtitulo = (
    ('Derecho a Credito Fiscal', 'Derecho a Credito Fiscal'),
    ('A Credito Fiscal', 'A Credito Fiscal'),
    ('Fiscal Ley Nro 366 del Libro Y la Factura', 'Fiscal Ley Nro 366 del Libro Y la Factura'),
    ('A Credito Fiscal-Venta Moneda Extranjera', 'A Credito Fiscal-Venta Moneda Extranjera'),
    ('Franca sin Derecho A Credito Fiscal', 'Franca sin Derecho A Credito Fiscal'),
    ('Espectaculo Publico Eventual', 'Espectaculo Publico Eventual'),
)

list_of_frases_pie = (
    ('Ley N° 453: Si se te ha vulnerado algún derecho puedes exigir la reposición o restauración.', 'Ley N° 453: Si se te ha vulnerado algún derecho puedes exigir la reposición o restauración.'),
    ('Ley N° 453: El proveedor deberá dar cumplimiento a las condiciones ofertadas.', 'Ley N° 453: El proveedor deberá dar cumplimiento a las condiciones ofertadas.'),
    ('Ley N° 453: Están prohibidas las prácticas comerciales abusivas, tienes derecho a denunciarlas.', 'Ley N° 453: Están prohibidas las prácticas comerciales abusivas, tienes derecho a denunciarlas.'),
    ('Ley N° 453: Tienes derecho a recibir información que te proteja de la publicidad engañosa.', 'Ley N° 453: Tienes derecho a recibir información que te proteja de la publicidad engañosa.'),
    ('Ley N° 453: Puedes acceder a la reclamación cuando tus derechos han sido vulnerados.', 'Ley N° 453: Puedes acceder a la reclamación cuando tus derechos han sido vulnerados.'),
    ('Ley N° 453: Los contratos de adhesión deben redactarse en términos claros, comprensibles, legibles y deben informar todas las facilidades y limitaciones.', 'Ley N° 453: Los contratos de adhesión deben redactarse en términos claros, comprensibles, legibles y deben informar todas las facilidades y limitaciones.'),
    ('Ley N° 453: Se debe promover el consumo solidario, justo, en armonía con la Madre Tierra y precautelando el hábitat, en el marco del Vivir Bien.', 'Ley N° 453: Se debe promover el consumo solidario, justo, en armonía con la Madre Tierra y precautelando el hábitat, en el marco del Vivir Bien.'),
    ('Ley N° 453: El proveedor de productos debe habilitar medios e instrumentos para efectuar consultas y reclamaciones.', 'Ley N° 453: El proveedor de productos debe habilitar medios e instrumentos para efectuar consultas y reclamaciones.'),
    ('Ley N° 453: El proveedor debe brindar atención sin discriminación, con respeto, calidez y cordialidad a los usuarios y consumidores.', 'Ley N° 453: El proveedor debe brindar atención sin discriminación, con respeto, calidez y cordialidad a los usuarios y consumidores.'),
    ('Ley N° 453: Los servicios deben suministrarse en condiciones de inocuidad, calidad y seguridad.' , 'Ley N° 453: Los servicios deben suministrarse en condiciones de inocuidad, calidad y seguridad.'),
    ('Ley N° 453: Tienes derecho a un trato equitativo sin discriminación en la oferta de servicios.', 'Ley N° 453: Tienes derecho a un trato equitativo sin discriminación en la oferta de servicios.'), 
    ('Ley N° 453: El proveedor deberá suministrar el servicio en las modalidades y términos ofertados o convenidos.', 'Ley N° 453: El proveedor deberá suministrar el servicio en las modalidades y términos ofertados o convenidos.'),
    ('Ley N° 453: En caso de incumplimiento a lo ofertado o convenido, el proveedor debe reparar o sustituir el servicio.', 'Ley N° 453: En caso de incumplimiento a lo ofertado o convenido, el proveedor debe reparar o sustituir el servicio.'),
    ('Ley N° 453: Tienes derecho a recibir información sobre las características y contenidos de los servicios que utilices.', 'Ley N° 453: Tienes derecho a recibir información sobre las características y contenidos de los servicios que utilices.'),
    ('Ley N° 453: La interrupción del servicio debe comunicarse con anterioridad a las Autoridades que correspondan y a los usuarios afectados.', 'Ley N° 453: La interrupción del servicio debe comunicarse con anterioridad a las Autoridades que correspondan y a los usuarios afectados.'),
    ('Ley N° 453: El proveedor de servicios debe habilitar medios e instrumentos para efectuar consultas y reclamaciones.', 'Ley N° 453: El proveedor de servicios debe habilitar medios e instrumentos para efectuar consultas y reclamaciones.'),
    ('Ley N° 453: El proveedor debe exhibir certificaciones de habilitación o documentos que acrediten las capacidades u ofertas de servicios especializados.', 'Ley N° 453: El proveedor debe exhibir certificaciones de habilitación o documentos que acrediten las capacidades u ofertas de servicios especializados.'),
    ('Ley N° 453: Los productos deben suministrarse en condiciones de inocuidad, calidad y seguridad.', 'Ley N° 453: Los productos deben suministrarse en condiciones de inocuidad, calidad y seguridad.'),
    ('Ley N° 453: Está prohibido importar, distribuir o comercializar productos expirados o prontos a expirar.', 'Ley N° 453: Está prohibido importar, distribuir o comercializar productos expirados o prontos a expirar.'),
    ('Ley N° 453: Está prohibido importar, distribuir o comercializar productos prohibidos o retirados en el país de origen por atentar a la integridad física', 'Ley N° 453: Está prohibido importar, distribuir o comercializar productos prohibidos o retirados en el país de origen por atentar a la integridad física'),
    ('Ley N° 453: Tienes derecho a recibir información sobre las características y contenidos de los productos que consumes.', 'Ley N° 453: Tienes derecho a recibir información sobre las características y contenidos de los productos que consumes.'),
    ('Ley N° 453: Tienes derecho a un trato equitativo sin discriminación en la oferta de productos.', 'Ley N° 453: Tienes derecho a un trato equitativo sin discriminación en la oferta de productos.'),
    ('Ley N° 453: El proveedor deberá entregar el producto en las modalidades y términos ofertados o convenidos.', 'Ley N° 453: El proveedor deberá entregar el producto en las modalidades y términos ofertados o convenidos.'),
    ('Ley N° 453: En caso de incumplimiento a lo ofertado o convenido, el proveedor debe reparar o sustituir el producto.', 'Ley N° 453: En caso de incumplimiento a lo ofertado o convenido, el proveedor debe reparar o sustituir el producto.'),
    ('Ley N° 453: Los alimentos declarados de primera necesidad deben ser suministrados de manera adecuada, oportuna, continua y a precio justo.', 'Ley N° 453: Los alimentos declarados de primera necesidad deben ser suministrados de manera adecuada, oportuna, continua y a precio justo.'),
    ('Ley N° 453: El prestador de servicio médico debe brindar atención de calidad al paciente.', 'Ley N° 453: El prestador de servicio médico debe brindar atención de calidad al paciente.'),
    ('Ley N° 453: Cuando lo solicite el paciente, se debe informar los resultados de exámenes, diagnósticos y estudios de laboratorio.', 'Ley N° 453: Cuando lo solicite el paciente, se debe informar los resultados de exámenes, diagnósticos y estudios de laboratorio.'),
    ('Ley N° 453: El prestador de servicio médico debe prescribir medicamentos debidamente autorizados por el Ministerio de Salud.', 'Ley N° 453: El prestador de servicio médico debe prescribir medicamentos debidamente autorizados por el Ministerio de Salud.'),
    ('Ley N° 453: Se debe otorgar el auxilio y atención necesarios en casos de urgencia o emergencia hospitalaria, sin aducir excusa alguna.', 'Ley N° 453: Se debe otorgar el auxilio y atención necesarios en casos de urgencia o emergencia hospitalaria, sin aducir excusa alguna.'),
    ('Ley N° 453: Se debe brindar alternativas de pago por servicios utilizados en emergencia médica u hospitalaria, no pudiendo retenerse al usuario por', 'Ley N° 453: Se debe brindar alternativas de pago por servicios utilizados en emergencia médica u hospitalaria, no pudiendo retenerse al usuario por'),
    ('Ley N° 453: Tienes derecho a denunciar la existencia de productos y servicios que pongan en riesgo tu salud o integridad física.', 'Ley N° 453: Tienes derecho a denunciar la existencia de productos y servicios que pongan en riesgo tu salud o integridad física.'),
    ('Ley N° 453: La entidad financiera tiene la obligación de promover la educación financiera.', 'Ley N° 453: La entidad financiera tiene la obligación de promover la educación financiera.'),
    ('Ley N° 453: La entidad financiera debe facilitar en cualquier momento y gratuitamente, toda información de los movimientos bancarios, financieros', 'Ley N° 453: La entidad financiera debe facilitar en cualquier momento y gratuitamente, toda información de los movimientos bancarios, financieros'),
    ('Ley N° 453: La entidad financiera debe informar por escrito los motivos por los cuales se denegó un crédito.', 'Ley N° 453: La entidad financiera debe informar por escrito los motivos por los cuales se denegó un crédito.'),
    ('Ley N° 453: Los medios de comunicación deben difundir mensajes o programas de educación de consumo responsable y sustentable.', 'Ley N° 453: Los medios de comunicación deben difundir mensajes o programas de educación de consumo responsable y sustentable.'),
    ('Ley N° 453: Los medios de comunicación deben promover el respeto de los derechos de los usuarios y consumidores.', 'Ley N° 453: Los medios de comunicación deben promover el respeto de los derechos de los usuarios y consumidores.'),
    ('Ley N° 453: Las publicaciones, mensajes e imágenes no deben promover la sumisión o explotación de las mujeres.', 'Ley N° 453: Las publicaciones, mensajes e imágenes no deben promover la sumisión o explotación de las mujeres.'),
    ('Ley N° 453: Las publicaciones, mensajes e imágenes no deben deshonrar y atentar contra la dignidad e imagen de la mujer.', 'Ley N° 453: Las publicaciones, mensajes e imágenes no deben deshonrar y atentar contra la dignidad e imagen de la mujer.'),
    ('Ley N° 453: Los medios de comunicación deben evitar contenidos inapropiados que vulneren la protección de niñas, niños y adolescentes.', 'Ley N° 453: Los medios de comunicación deben evitar contenidos inapropiados que vulneren la protección de niñas, niños y adolescentes.'),
)





CHOICET = (
('oficio', 'oficio'),
    ('carta', 'Carta'),
    ('1/2oficio', '1/2 oficio'),
    ('rollo', 'rollo'),
)


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    """renders horizontal radio buttons.
    found here:
    https://wikis.utexas.edu/display/~bm6432/Django-Modifying+RadioSelect+Widget+to+have+horizontal+buttons
    """

    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


FormatoFormSet = modelformset_factory(Formatodetalle, extra=0, fields=('impresion', 'facturacion', 'tamanio', 'frases_titulo', 'frases_subtitulo', 'frases_pie', 'sucursal' ))


class FormatoForm(FormatoFormSet):

    def add_fields(self, form, index):

        super(FormatoForm, self).add_fields(form, index)
        form.fields['sucursal'].widget = forms.HiddenInput()
        form.fields['impresion'] = forms.ChoiceField(choices=list_of_choices)
        form.fields['tamanio'] = forms.ChoiceField(choices=CHOICET, widget=forms.RadioSelect(renderer=HorizontalRadioRenderer))
        form.fields['facturacion'] = forms.ChoiceField(choices=list_of_facturacion)
        form.fields['frases_titulo'] = forms.ChoiceField(choices=list_of_frases_titulo)
        form.fields['frases_subtitulo'] = forms.ChoiceField(choices=list_of_frases_subtitulo)
        form.fields['frases_pie'] = forms.ChoiceField(choices=list_of_frases_pie)
