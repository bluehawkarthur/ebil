#!/usr/bin/python
# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter
from django.utils.translation import ugettext
from django.db.models import Avg, Sum, Max, Min

from apps.ventas.models import Venta


def WriteToAlmacen(weather_data, mes, total, town=None):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Reporte de almacenes")

    # excel styles
    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bold': True,
      
        'color': 'black',
        'align': 'center',
        'valign': 'vcenter',
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
        'align': 'left',
        'valign': 'top',
        'border': 1
    })

    # write title
    # if town:
    #     town_text = town.name
    # else:
    #     town_text = ugettext("all recorded towns")
    # title_text = u"{0}".format(ugettext("Reporte de almacenes"))
    # # merge cells
    # worksheet_s.merge_range('A2:D2', title_text, title)

    # write header
    worksheet_s.set_row(0, 35)
    worksheet_s.write(0, 0, ugettext("Item"), header)
    worksheet_s.write(0, 1, ugettext("Codigo fabrica"), header)
    worksheet_s.write(0, 2, ugettext("Almacen"), header)
    worksheet_s.write(0, 3, ugettext("Grupo"), header)
    worksheet_s.write(0, 4, ugettext("Subgrupo"), header)
    worksheet_s.write(0, 5, ugettext("Descripcion"), header)
    worksheet_s.write(0, 6, ugettext("Carac especial  1"), header)
    worksheet_s.write(0, 7, ugettext("Carac especial  2"), header)
    worksheet_s.write(0, 8, ugettext("Cantidad"), header)
    worksheet_s.write(0, 9, ugettext("Saldo minimo"), header)
    worksheet_s.write(0, 10, ugettext("Proveedor"), header)
    worksheet_s.write(0, 11, ugettext("Unidad"), header)
    worksheet_s.write(0, 12, ugettext("Costo unitario"), header)
    worksheet_s.write(0, 13, ugettext("Precio unitario"), header)
    worksheet_s.write(0, 14, ugettext("TOTAL COSTO"), header)
    worksheet_s.write(0, 15, ugettext("TOTAL PRECIO"), header)
    

    # column widths
    town_col_width = 18
    description_col_width = 10
    observations_col_width = 25
    total_costo = 0
    total_precio = 0
    # add data to the table
    for idx, data in enumerate(weather_data):
        row = 1 + idx
        # worksheet_s.write_number(row, 0, idx + 1, cell_center)
        total_costo += data.cantidad * data.costo_unitario
        total_precio += data.cantidad * data.precio_unitario

        worksheet_s.write(row, 0, data.codigo_item, cell_center)
        worksheet_s.write_string(row, 1, data.codigo_fabrica, cell)
        worksheet_s.write_number(row, 2, data.almacen, cell_center)
        worksheet_s.write_string(row, 3, data.grupo, cell_center)
        worksheet_s.write_string(row, 4, data.subgrupo, cell_center)
        worksheet_s.write_string(row, 5, data.descripcion, cell_center)
        worksheet_s.write_string(row, 6, data.carac_especial_1, cell_center)
        worksheet_s.write_string(row, 7, data.carac_especial_2, cell_center)
        worksheet_s.write_number(row, 8, data.cantidad, cell_center)
        worksheet_s.write_number(row, 9, data.saldo_min, cell_center)
        worksheet_s.write_string(row, 10, data.proveedor.razon_social, cell_center)
        worksheet_s.write_string(row, 11, data.unidad_medida, cell_center)
        worksheet_s.write_number(row, 12, data.costo_unitario, cell_center)
        worksheet_s.write_number(row, 13, data.precio_unitario, cell_center)
        worksheet_s.write_number(row, 14, data.cantidad * data.costo_unitario, cell_center)
        worksheet_s.write_number(row, 15, data.cantidad * data.precio_unitario, cell_center)





    # change column widths
    worksheet_s.set_column('A:A', 12) 
    worksheet_s.set_column('B:B', town_col_width)  # Town column
    worksheet_s.set_column('C:C', 11)  # Date column
    worksheet_s.set_column('D:D', description_col_width)  # Description column
    worksheet_s.set_column('E:E', 10)  # Max Temp column
    worksheet_s.set_column('F:F', 50)  # Min Temp column
    worksheet_s.set_column('G:G', 20)  # Wind Speed column
    worksheet_s.set_column('H:H', 20)  # Precipitation column
    worksheet_s.set_column('I:I', 11)  # Precipitation % column
    worksheet_s.set_column('J:J', 15)  # Observations column
    worksheet_s.set_column('K:K', 12)
    worksheet_s.set_column('M:M', 15)
    worksheet_s.set_column('N:N', 15)
    worksheet_s.set_column('O:O', 15)
    worksheet_s.set_column('P:P', 15)

    row = row + 1
   
    worksheet_s.write(row, 13, ugettext("TOTAL GENERAL"), cell_total)
    # worksheet_s.write_formula(row, 3, '=SUM(D6:D7)')
    worksheet_s.write(row, 14, total_costo, cell_total)
    worksheet_s.write(row, 15, total_precio, cell_total)


    # close workbook
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data
