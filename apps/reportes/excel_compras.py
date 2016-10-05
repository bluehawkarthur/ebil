#!/usr/bin/python
# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter
from django.utils.translation import ugettext
from django.db.models import Avg, Sum, Max, Min
import decimal
from apps.ventas.models import Venta


def WriteToCompras(weather_data, mes, total, empresa, town=None):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Libro de Compras")

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
    title_text = u"{0}".format(ugettext("LIBRO DE COMPRAS ESTANDAR"))
    # merge cells
    worksheet_s.merge_range('A2:L2', title_text, title)
    periodo = '%s %s' % ('PERIODO', mes)
    worksheet_s.merge_range('A3:L3', ugettext(periodo), title2)

    # write header
  
    razon_social = '%s %s' % ('Nombre o Razon Social:', empresa.razon_social)
    nit = '%s %s' % ('NIT:', empresa.nit)
    worksheet_s.merge_range('A4:D4', ugettext(razon_social), cell2)
  

    worksheet_s.merge_range('K4:M4', ugettext(nit), cell2)
  
    # worksheet_s.write(3, 0, ugettext("Nombre o Razon Social:"), cell)
    # worksheet_s.write(3, 1, ugettext(mes), cell)
    # format = workbook.add_format()
    header.set_text_wrap()
    worksheet_s.write(6, 0, ugettext("Nro"), header)
    worksheet_s.write(6, 1, ugettext("Fecha de la Factura"), header)
    worksheet_s.write(6, 2, ugettext("NIT Proveedor"), header)
    worksheet_s.write(6, 3, ugettext("Nombre o Razon Social"), header)
    worksheet_s.write(6, 4, ugettext("Nro de la Factura"), header)
    worksheet_s.write(6, 5, ugettext("Nro de Autorizacion"), header)
    worksheet_s.write(6, 6, ugettext("Importe Total de la Compra"), header)
    worksheet_s.write(6, 7, ugettext("Importe No Sujeto a Credito Fiscal"), header)
    worksheet_s.write(6, 8, ugettext("Subtotal"), header)
    worksheet_s.write(6, 9, ugettext("Descuentos Bonificaciones y Rebajas"), header)
    worksheet_s.write(6, 10, ugettext("Importe Base para Credito Fiscal"), header)
    worksheet_s.write(6, 11, ugettext("Credito Fiscal I.V.A."), header)
    worksheet_s.write(6, 12, ugettext("Codigo de Control"), header)
    worksheet_s.write(6, 13, ugettext("Tipo de Compra"), header)

    # column widths
    town_col_width = 15
    neto_total = 0
    cf_total = 0
    noscf_total = 0
    descuento_total = 0
    importe_base_total = 0
    # add data to the table
    for idx, data in enumerate(weather_data):
        row = 7 + idx
        neto = data.total - data.ice - data.excentos
        importe_base = neto - data.descuento
        cf = importe_base * 13 / 100
        cf_total = cf_total + cf
        neto_total = neto_total + neto
        noscf = data.ice + data.excentos

        noscf_total = noscf_total + noscf
        descuento_total = descuento_total + data.descuento
        importe_base_total = importe_base_total + importe_base

        worksheet_s.write_number(row, 0, idx + 1, cell_center)

        worksheet_s.write(row, 1, data.fecha.strftime('%d/%m/%Y'), cell_center)
        worksheet_s.write_number(row, 2, data.nit, cell)
        worksheet_s.write_string(row, 3, data.razon_social, cell)
        worksheet_s.write_number(row, 4, data.nro_factura, cell)
        worksheet_s.write_string(row, 5, data.nro_autorizacion, cell)
        worksheet_s.write_number(row, 6, data.total, cell_center)
        worksheet_s.write_number(row, 7, noscf, cell_center)
        worksheet_s.write_number(row, 8, neto, cell_center)
        worksheet_s.write_number(row, 9, data.descuento, cell_center)
        worksheet_s.write_number(row, 10, importe_base, cell_center)
        worksheet_s.write_number(row, 11, cf, cell_center)
        worksheet_s.write_string(row, 12, data.cod_control, cell)
        worksheet_s.write_string(row, 13, '1', cell_center)



    # change column widths
    worksheet_s.set_column('B:B', town_col_width)  # Town column
    worksheet_s.set_row(6, 30)
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
    worksheet_s.write(row, 5, ugettext("TOTAL"), cell_total)
    # worksheet_s.write_formula(row, 3, '=SUM(D6:D7)')
    worksheet_s.write(row, 6, total, cell_total)
    worksheet_s.write(row, 7, noscf_total, cell_total)
    worksheet_s.write(row, 8, neto_total, cell_total)
    worksheet_s.write(row, 9, descuento_total, cell_total)
    worksheet_s.write(row, 10, importe_base_total, cell_total)
    worksheet_s.write(row, 11, cf_total, cell_total)

    # close workbook
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data

