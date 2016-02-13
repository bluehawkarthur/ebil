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


class PdfPrint:

    # initialize class
    def __init__(self, buffer, pageSize):
        self.buffer = buffer
        # default format is A4
        if pageSize == 'A4':
            self.pageSize = A4
        elif pageSize == 'Letter':
            self.pageSize = letter
        self.width, self.height = self.pageSize

    def pageNumber(self, canvas, doc):
        number = canvas.getPageNumber()
        canvas.drawCentredString(100 * mm, 15 * mm, str(number))



    def report(self, weather_history, title, total, mes):
        # set some characteristics for pdf document
        doc = SimpleDocTemplate(
            self.buffer,
            rightMargin=72,
            leftMargin=72,
            topMargin=30,
            bottomMargin=72,
            pagesize=self.pageSize)

        # a collection of styles offer by the library
        styles = getSampleStyleSheet()
        # add custom paragraph style
        styles.add(ParagraphStyle(
            name="TableHeader", fontSize=11, alignment=TA_CENTER,
            fontName="FreeSansBold"))
        styles.add(ParagraphStyle(
            name="ParagraphTitle", fontSize=11, alignment=TA_JUSTIFY,
            fontName="FreeSansBold"))
        styles.add(ParagraphStyle(
            name="Justify", alignment=TA_JUSTIFY, fontName="FreeSans"))
        # list used for elements added into document
        data = []
        data.append(Paragraph(title, styles['Title']))
        # insert a blank space
        data.append(Spacer(1, 12))
        table_data = []

        # table header
        table_data.append([
            Paragraph('Nro', styles['TableHeader']),
            Paragraph('Fecha', styles['TableHeader']),
            Paragraph('Cliente', styles['TableHeader']),
            Paragraph('Monto', styles['TableHeader'])])
        date_month = '%s %s' % ('PERIODO', mes)
        data.append(Paragraph(date_month, styles['Justify']))

        data.append(Spacer(1, 12))

        tabla1 = 34
        totales = 0
        count = 0
        num = weather_history.count()

        for i in range(0, num):
            count = count + 1
            if i < tabla1:
                totales = totales + weather_history[i].total

            if i == tabla1:

                table_data.append(['', '', Paragraph('Subtotal', styles['TableHeader']), totales])
       
                totales = weather_history[i].total

                tabla1 = tabla1 + 38

            # add a row to table
            table_data.append(
                [count, weather_history[i].fecha,
                 Paragraph(weather_history[i].razon_social, styles['Justify']),
                 u"{0}".format(weather_history[i].total)])

        table_data.append(['', '', Paragraph('Total', styles['TableHeader']), total])
        # create table
        wh_table = Table(table_data, colWidths=[doc.width / 7.0] * 7, repeatRows = 1)
        wh_table.hAlign = 'LEFT'
        wh_table.setStyle(TableStyle(
            [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
             ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
             ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
             ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))
        data.append(wh_table)
        data.append(Spacer(1, 48))

        # create document
        doc.build(data, onFirstPage=self.pageNumber,
                  onLaterPages=self.pageNumber)
        pdf = self.buffer.getvalue()
        self.buffer.close()
        return pdf
