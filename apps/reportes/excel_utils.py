#!/usr/bin/python
# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter
from django.utils.translation import ugettext
from django.db.models import Avg, Sum, Max, Min

from apps.ventas.models import Venta


def WriteToExcel(weather_data, mes, total, town=None):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Summary")

    # excel styles
    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    cell = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })
    cell_total = workbook.add_format({
        'bold': True,
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })
    cell_center = workbook.add_format({
        'align': 'center',
        'valign': 'top',
        'border': 1
    })

    # write title
    if town:
        town_text = town.name
    else:
        town_text = ugettext("all recorded towns")
    title_text = u"{0}".format(ugettext("REPORTE DE VENTAS"))
    # merge cells
    worksheet_s.merge_range('A2:D2', title_text, title)

    # write header
    worksheet_s.write(2, 0, ugettext("PERIODO"), cell)
    worksheet_s.write(2, 1, ugettext(mes), cell)
    worksheet_s.write(4, 0, ugettext("No"), header)
    worksheet_s.write(4, 1, ugettext("Fecha"), header)
    worksheet_s.write(4, 2, ugettext("Cliente"), header)
    worksheet_s.write(4, 3, ugettext("Monto"), header)

    # column widths
    town_col_width = 10
    description_col_width = 10
    observations_col_width = 25

    # add data to the table
    for idx, data in enumerate(weather_data):
        row = 5 + idx
        worksheet_s.write_number(row, 0, idx + 1, cell_center)
        

        worksheet_s.write(row, 1, data.fecha.strftime('%d/%m/%Y'), cell_center)
        worksheet_s.write_string(row, 2, data.razon_social, cell)
        if len(data.razon_social) > description_col_width:
            description_col_width = len(data.razon_social)

        worksheet_s.write_number(row, 3, data.total, cell_center)
       

       

    # change column widths
    worksheet_s.set_column('B:B', town_col_width)  # Town column
    worksheet_s.set_column('C:C', 11)  # Date column
    worksheet_s.set_column('D:D', description_col_width)  # Description column
    worksheet_s.set_column('E:E', 10)  # Max Temp column
    worksheet_s.set_column('F:F', 10)  # Min Temp column
    worksheet_s.set_column('G:G', 10)  # Wind Speed column
    worksheet_s.set_column('H:H', 11)  # Precipitation column
    worksheet_s.set_column('I:I', 11)  # Precipitation % column
    worksheet_s.set_column('J:J', observations_col_width)  # Observations column

    row = row + 1
   
    worksheet_s.write(row, 2, ugettext("TOTAL"), cell_total)
    # worksheet_s.write_formula(row, 3, '=SUM(D6:D7)')
    worksheet_s.write(row, 3, total, cell_total)


    # close workbook
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data


def compute_rows(text, width):
    if len(text) < width:
        return 1
    phrases = text.replace('\r', '').split('\n')

    rows = 0
    for phrase in phrases:
        if len(phrase) < width:
            rows = rows + 1
        else:
            words = phrase.split(' ')
            temp = ''
            for idx, word in enumerate(words):
                temp = temp + word + ' '
                # check if column width exceeded
                if len(temp) > width:
                    rows = rows + 1
                    temp = '' + word + ' '
                # check if it is not the last word
                if idx == len(words) - 1 and len(temp) > 0:
                    rows = rows + 1
    return rows
