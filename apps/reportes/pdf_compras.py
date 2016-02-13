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
from reportlab.lib.pagesizes import letter, A4
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


class PdfCompras:

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
            bottomMargin=50,
            pagesize=self.pageSize)

        # a collection of styles offer by the library
        styles = getSampleStyleSheet()
        # add custom paragraph style
        styles.add(ParagraphStyle(
            name="TableHeader", fontSize=8, alignment=TA_CENTER,
            fontName="FreeSansBold"))

        styles.add(ParagraphStyle(
            name="Title2", fontSize=10, alignment=TA_CENTER,
            fontName="FreeSansBold"))

        styles.add(ParagraphStyle(
            name="Title3", fontSize=8,
            fontName="FreeSansBold"))

        styles.add(ParagraphStyle(
            name="ParagraphTitle", fontSize=11, alignment=TA_JUSTIFY,
            fontName="FreeSansBold"))

        styles.add(ParagraphStyle(
            name="Justify", textTransform='lowercase', alignment=TA_JUSTIFY, fontName="FreeSans"))
        # list used for elements added into document
        data = []
        data.append(Paragraph(title, styles['Title']))

        date_month = '%s %s' % ('PERIODO', mes)
        data.append(Paragraph(date_month, styles['Title2']))
        # insert a blank space
        data.append(Spacer(1, 5))
        table_data = []
        table_data2 = []
        # table header
        table_data.append([
            Paragraph('Nro', styles['TableHeader']),
            Paragraph('Fecha', styles['TableHeader']),
            Paragraph('Nit', styles['TableHeader']),
            Paragraph('Nombre Razon Social', styles['TableHeader']),
            Paragraph('Factura', styles['TableHeader']),
            Paragraph('No Autorizacion', styles['TableHeader']),
            Paragraph('Codigo de Control', styles['TableHeader']),
            Paragraph('Total factura', styles['TableHeader']),
            Paragraph('ICE', styles['TableHeader']),
            Paragraph('Excentos', styles['TableHeader']),
            Paragraph('Neto', styles['TableHeader']),
            Paragraph('Credito Fiscal', styles['TableHeader']),
            ])

        date_month = '%s %s' % ('PERIODO', mes)
        # data.append(Paragraph('Nombre o Razon Social: EVEREST', styles['Justify']))
        # data.append(Paragraph('CASA MATRIZ', styles['Justify']))

        table_data2.append([Paragraph('Nombre o Razon Social: EVEREST2', styles['Title3']), '', Paragraph('NIT.: 1021325022', styles['Title3'])])
        table_data2.append([Paragraph('CASA MATRIZ', styles['Title3']), '', Paragraph('CALLE ESTEBAN ARCE', styles['Title3'])])

        data.append(Spacer(1, 12))

        tabla1 = 19
        totales = 0
        count = 0
        num = weather_history.count()
        neto_total = 0
        cf_total = 0

        neto_subtotal = 0
        cf_subtotal = 0

        for i in range(0, num):
            count = count + 1
            neto = weather_history[i].total - weather_history[i].ice - weather_history[i].excentos
            cf = neto * 13 / 100

            if i < tabla1:
                totales = totales + weather_history[i].total
                cf_subtotal = cf_subtotal + cf
                neto_subtotal = neto_subtotal + neto

            if i == tabla1:

                table_data.append(['', '', '', '', '', '', Paragraph('Subtotal', styles['TableHeader']), totales, '-', '-', neto_subtotal, cf_subtotal])
       
                totales = weather_history[i].total
                cf_subtotal = cf
                neto_subtotal = neto

                tabla1 = tabla1 + 23

            cf_total = cf_total + cf
            neto_total = neto_total + neto
            # add a row to table
            table_data.append([
                count,
                weather_history[i].fecha,
                weather_history[i].nit,
                Paragraph(weather_history[i].razon_social, styles['Justify']),
                weather_history[i].nro_factura,
                weather_history[i].nro_autorizacion,
                weather_history[i].cod_control,
                u"{0}".format(weather_history[i].total),
                weather_history[i].ice,
                weather_history[i].excentos,
                neto,
                cf,
            ])

        table_data.append(['', '', '', '', '', '', Paragraph('Total', styles['TableHeader']), total, '-', '-', neto_total, cf_total])
        # create table
        wh_table = Table(table_data, colWidths=[doc.width / 12.0] * 7, repeatRows = 1)

        wh_table2 = Table(table_data2, colWidths=[doc.width / 2.5] * 7)
        wh_table2.hAlign = 'LEFT'

        wh_table.hAlign = 'LEFT'
        wh_table.setStyle(TableStyle(
            [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
             ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
             ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
             ('FONTSIZE', (0, 0), (-1, -1), 8),
             ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))

        wh_table2.setStyle(TableStyle(
            [('VALIGN', (0, 0), (-1, 0), 'MIDDLE')]))

        data.append(wh_table2)
        data.append(Spacer(1, 20))
        data.append(wh_table)
        data.append(Spacer(1, 48))

        # create document
        doc.build(data, onFirstPage=self.pageNumber,
                  onLaterPages=self.pageNumber)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf
