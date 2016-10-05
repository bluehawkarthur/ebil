#!/usr/bin/python
# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter
from django.utils.translation import ugettext
from django.db.models import Avg, Sum, Max, Min
import decimal
from apps.ventas.models import Venta


def WriteToVentas(weather_data, mes, total, town=None):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Libro de Ventas")

    # excel styles
    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })

    title2 = workbook.add_format({
        'bold': True,
        'font_size': 12,
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
    cell2 = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'bold': True
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

    cell_center2 = workbook.add_format({
        'align': 'center',
        'valign': 'top',
        'bold': True
    })

    # write title
    if town:
        town_text = town.name
    else:
        town_text = ugettext("all recorded towns")
    title_text = u"{0}".format(ugettext("LIBRO DE VENTAS"))
    # merge cells
    worksheet_s.merge_range('A2:I2', title_text, title)
    periodo = '%s %s' % ('PERIODO', mes)
    worksheet_s.merge_range('A3:I3', ugettext(periodo), title2)

    # write header
    worksheet_s.merge_range('A4:D4', ugettext("Nombre o Razon Social: EVEREST"), cell2)
    worksheet_s.merge_range('A5:C5', ugettext("CASA MATRIZ"), cell_center2)

    worksheet_s.merge_range('H4:I4', ugettext("NIT.: 1021325022"), cell_center2)
    worksheet_s.merge_range('H5:I5', ugettext("CALLE ESTEBAN ARCE"), cell_center2)
    # worksheet_s.write(3, 0, ugettext("Nombre o Razon Social:"), cell)
    # worksheet_s.write(3, 1, ugettext(mes), cell)

    worksheet_s.write(6, 0, ugettext("No"), header)
    worksheet_s.write(6, 1, ugettext("Fecha"), header)
    worksheet_s.write(6, 2, ugettext("Nit"), header)
    worksheet_s.write(6, 3, ugettext("Nombre Razon Social"), header)
    worksheet_s.write(6, 4, ugettext("Total factura"), header)
    worksheet_s.write(6, 5, ugettext("ICE"), header)
    worksheet_s.write(6, 6, ugettext("Excentos"), header)
    worksheet_s.write(6, 7, ugettext("Neto"), header)
    worksheet_s.write(6, 8, ugettext("Credito Fiscal"), header)

    # column widths
    town_col_width = 10
    neto_total = 0
    cf_total = 0
    # add data to the table
    for idx, data in enumerate(weather_data):
        row = 7 + idx
        neto = data.total - data.ice - data.excentos
        cf = neto * 13 / 100
        cf_total = cf_total + cf
        neto_total = neto_total + neto
        worksheet_s.write_number(row, 0, idx + 1, cell_center)

        worksheet_s.write(row, 1, data.fecha.strftime('%d/%m/%Y'), cell_center)
        worksheet_s.write_number(row, 2, data.nit, cell)
        worksheet_s.write_string(row, 3, data.razon_social, cell)
        worksheet_s.write_number(row, 4, data.total, cell_center)
        worksheet_s.write_number(row, 5, data.ice, cell_center)
        worksheet_s.write_number(row, 6, data.excentos, cell_center)
        worksheet_s.write_number(row, 7, neto, cell_center)
        worksheet_s.write_number(row, 8, cf, cell_center)


    # change column widths
    worksheet_s.set_column('B:B', town_col_width)  # Town column
    worksheet_s.set_column('C:C', 11)  # Date column
    worksheet_s.set_column('D:D', 25)  # Description column
    worksheet_s.set_column('E:E', 12)  # Max Temp column
    worksheet_s.set_column('F:F', 15)  # Min Temp column
    worksheet_s.set_column('G:G', 15)  # Wind Speed column
    worksheet_s.set_column('H:H', 11)  # Precipitation column
    worksheet_s.set_column('I:I', 11)  # Precipitation % column
    worksheet_s.set_column('J:J', 10)  # Observations column
    worksheet_s.set_column('L:L', 12)

    row = row + 1
    worksheet_s.write(row, 3, ugettext("TOTAL"), cell_total)
    # worksheet_s.write_formula(row, 3, '=SUM(D6:D7)')
    worksheet_s.write(row, 4, total, cell_total)
    worksheet_s.write(row, 5, ugettext("-"), cell_total)
    worksheet_s.write(row, 6, ugettext("-"), cell_total)
    worksheet_s.write(row, 7, neto_total, cell_total)
    worksheet_s.write(row, 8, cf_total, cell_total)

    # close workbook
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data

