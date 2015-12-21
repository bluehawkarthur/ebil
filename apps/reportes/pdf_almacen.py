#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.linecharts import SampleHorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter, A4, B4
from reportlab.lib.units import mm
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table,\
    TableStyle
import os

from django.conf import settings

from .utils import get_temperatures, get_wind_speed, get_str_days,\
    get_random_colors, precip_prob_sum, get_percentage
legendcolors = get_random_colors(10)

pdfmetrics.registerFont(TTFont('FreeSans',os.path.join(settings.BASE_DIR, 'static', 'font', 'FreeSans.ttf')))

# pdfmetrics.registerFont(TTFont('FreeSans', STATIC_ROOT + 'fonts/FreeSans.ttf'))
pdfmetrics.registerFont(TTFont('FreeSansBold',os.path.join(settings.BASE_DIR, 'static', 'font', 'FreeSansBold.ttf')))

# pdfmetrics.registerFont(
#     TTFont('FreeSansBold', STATIC_ROOT + 'fonts/FreeSansBold.ttf'))


class PdfAlmacen:

    # initialize class
    def __init__(self, buffer, pageSize):
        self.buffer = buffer
        # default format is A4
        if pageSize == 'A4':
            self.pageSize = (29.7*cm, 21*cm)
        elif pageSize == 'Letter':
            self.pageSize = letter
        self.width, self.height = self.pageSize


    def pageNumber(self, canvas, doc):
        number = canvas.getPageNumber()
        canvas.drawCentredString(150 * mm, 15 * mm, str(number))



    def report(self, weather_history, title, total, mes):
        # set some characteristics for pdf document
        doc = SimpleDocTemplate(
            self.buffer,
            rightMargin=50,
            leftMargin=50,
            topMargin=30,
            bottomMargin=72,
            pagesize=self.pageSize)

        # a collection of styles offer by the library
        styles = getSampleStyleSheet()
        # add custom paragraph style
        styles.add(ParagraphStyle(
            name="TableHeader", fontSize=8, alignment=TA_CENTER,
            fontName="FreeSansBold"))
        styles.add(ParagraphStyle(
            name="ParagraphTitle", fontSize=8, alignment=TA_JUSTIFY,
            fontName="FreeSansBold"))
        styles.add(ParagraphStyle(
            name="Justify", fontSize=8, alignment=TA_JUSTIFY, fontName="FreeSans"))
        # list used for elements added into document
        data = []
        data.append(Paragraph(title, styles['Title']))
        # insert a blank space
        data.append(Spacer(1, 12))
        table_data = []

        # table header
        table_data.append([
            Paragraph('Item', styles['TableHeader']),
            Paragraph('Codigo fabrica', styles['TableHeader']),
            Paragraph('Almacen', styles['TableHeader']),
            Paragraph('Grupo', styles['TableHeader']),
            Paragraph('Subgrupo', styles['TableHeader']),
            Paragraph('Descripcion', styles['TableHeader']),
            Paragraph('Carac especial  1', styles['TableHeader']),
            Paragraph('Carac especial  2', styles['TableHeader']),
            Paragraph('Cantidad', styles['TableHeader']),
            Paragraph('Saldo minimo', styles['TableHeader']),
            Paragraph('Proveedor', styles['TableHeader']),
            Paragraph('Unidad', styles['TableHeader']),
            Paragraph('Costo unitario', styles['TableHeader']),
            Paragraph('Precio unitario', styles['TableHeader']),
            Paragraph('TOTAL COSTO', styles['TableHeader']),
            Paragraph('TOTAL PRECIO', styles['TableHeader'])
            ])

        data.append(Spacer(1, 12))

        tabla1 = 8
        totales = 0
        count = 0
        num = weather_history.count()
        costotal = 0
        costotal2 = 0
        totalprecio = 0
        totalprecio2 = 0
        for i in range(0, num):
            count = count + 1
            if i < tabla1:
                # totales = totales + weather_history[i].total
                costotal2 +=  weather_history[i].cantidad * weather_history[i].costo_unitario
                totalprecio2 += weather_history[i].cantidad * weather_history[i].precio_unitario
                # totales = 1
            if i == tabla1:

                table_data.append(['', '', '','','','','','','','','','','', Paragraph('Subtotal', styles['TableHeader']), costotal2, totalprecio2])
       
                costotal2 =  weather_history[i].cantidad * weather_history[i].costo_unitario
                totalprecio2 = weather_history[i].cantidad * weather_history[i].precio_unitario
                tabla1 = tabla1 + 13

            costotal +=  weather_history[i].cantidad * weather_history[i].costo_unitario
            totalprecio += weather_history[i].cantidad * weather_history[i].precio_unitario

            descripcion = weather_history[i].descripcion
            desctruncate = (descripcion[:20] + '..') if len(descripcion) > 20 else descripcion
            # add a row to table
            table_data.append([
                Paragraph(weather_history[i].codigo_item, styles['Justify']),
                Paragraph(weather_history[i].codigo_fabrica, styles['Justify']),
                weather_history[i].almacen,
                Paragraph(weather_history[i].grupo, styles['Justify']),
                Paragraph(weather_history[i].subgrupo, styles['Justify']),
                # u"{0}".format(weather_history[i].subgrupo), 
                Paragraph(desctruncate, styles['Justify']),
                Paragraph(weather_history[i].carac_especial_1, styles['Justify']),
                Paragraph(weather_history[i].carac_especial_2, styles['Justify']),
                weather_history[i].cantidad,
                weather_history[i].saldo_min,
                Paragraph(weather_history[i].proveedor.razon_social, styles['Justify']),
                Paragraph(weather_history[i].unidad_medida, styles['Justify']),
                weather_history[i].costo_unitario,
                weather_history[i].precio_unitario,
                weather_history[i].cantidad * weather_history[i].costo_unitario,
                weather_history[i].cantidad * weather_history[i].precio_unitario,
            ])

        table_data.append(['', '', '','','','','','','','','','','', Paragraph('TOTAL', styles['TableHeader']), costotal, totalprecio])
        # create table
   
        wh_table = Table(table_data, colWidths=[doc.width / 16.0] * 7, repeatRows = 1)
        wh_table.hAlign = 'LEFT'

        wh_table.setStyle(TableStyle(
            [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
             ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
             ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
             ('ALIGNMENT', (0, 0), (-1, -1), 'CENTRE'),
             ('FONTSIZE', (0,0), (-1, -1), 8),
             ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))

        data.append(wh_table)
        data.append(Spacer(1, 48))
        # create document
        doc.build(data, onFirstPage=self.pageNumber,
                  onLaterPages=self.pageNumber)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf
