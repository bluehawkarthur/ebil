#!/usr/bin/python
# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter
from django.utils.translation import ugettext
from django.db.models import Avg, Sum, Max, Min

from apps.bancarizacion.models import BancarizacionVentas


def WriteToBancarizacionVentas(weather_data, mes, total, town=None):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Libro bancar_venat")

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

    # write header

    worksheet_s.set_row(0, 35)
    worksheet_s.write(0, 0, ugettext("Fecha de Venta"), header)
    worksheet_s.write(0, 1, ugettext("Modalidad de  la transaccion"), header)
    worksheet_s.write(0, 2, ugettext("Nro. De Cta. Doc. de pago"), header)
    worksheet_s.write(0, 3, ugettext("Fecha fact. DUE/Fecha Doc."), header)
    worksheet_s.write(0, 4, ugettext("Monto pagado en Doc. De pago"), header)
    worksheet_s.write(0, 5, ugettext("Tipo Transaccion"), header)
    worksheet_s.write(0, 6, ugettext("Monto acumulado"), header)
    worksheet_s.write(0, 7, ugettext("Nro. De fact. DUE/Nro. Doc."), header)
    worksheet_s.write(0, 8, ugettext("NIT Entidad Financiera"), header)
    worksheet_s.write(0, 9, ugettext("Monto fact./Monto Doc."), header)
    worksheet_s.write(0, 10, ugettext("Nro. de Documento de pago"), header)
    worksheet_s.write(0, 11, ugettext("Nro. de Autorizacion de la Fact."), header)
    worksheet_s.write(0, 12, ugettext("Tipo de Doc. de Pago"), header)
    worksheet_s.write(0, 13, ugettext("Tipo de documento"), header)
    worksheet_s.write(0, 14, ugettext("NIT/CI del cliente"), header)
    worksheet_s.write(0, 15, ugettext("Fecha del documento de pago"), header)
    worksheet_s.write(0, 16, ugettext("Razon Social Cliente"), header)

    
    # column widths
    town_col_width = 18
    description_col_width = 10
    observations_col_width = 25
    total_costo = 0
    total_precio = 0 
    # add data to the table
    for idx, data in enumerate(weather_data):
        row = 1 + idx
        worksheet_s.write_string(row, 0, data.venta_fecha.strftime('%d/%m/%Y'), cell_center)
        worksheet_s.write_string(row, 1, data.modalidad_d_la_transaccion, cell_center)
        worksheet_s.write_number(row, 2, data.nro_de_cta_doc_de_pago, cell_center)
        worksheet_s.write_string(row, 3, data.fecha_fact_dui_fecha_doc.strftime('%d/%m/%Y'), cell_center)
        worksheet_s.write_number(row, 4, data.monto_pagado_en_doc_d_pago, cell_center)
        worksheet_s.write_string(row, 5, data.tipo_transaccion, cell_center)
        worksheet_s.write_number(row, 6, data.monto_acumulado, cell_center)
        worksheet_s.write_number(row, 7, data.nro_d_fact_dui_nro_doc, cell_center)
        worksheet_s.write_number(row, 8, data.nit_entidad_inanciera, cell_center)
        worksheet_s.write_string(row, 9, data.monto_fact_monto_doc, cell_center)
        worksheet_s.write_number(row, 10, data.nro_d_documento_de_pago, cell_center)
        worksheet_s.write_number(row, 11, data.nro_de_auturizacion_d_fact, cell_center)
        worksheet_s.write_string(row, 12, data.tipo_de_doc_d_pago, cell_center)
        worksheet_s.write_string(row, 13, data.tipo_de_documento, cell_center)
        worksheet_s.write_number(row, 14, data.nit_ci_d_cliente, cell_center)
        worksheet_s.write_string(row, 15, data.fecha_d_documento_d_pago.strftime('%d/%m/%Y'), cell_center)
        worksheet_s.write_string(row, 16, data.razon_social_cliente, cell_center)


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
    worksheet_s.set_column('P:P', 15)

    row = row + 1
   
    # worksheet_s.write(row, 13, ugettext("TOTAL GENERAL"), cell_total)
    # worksheet_s.write_formula(row, 3, '=SUM(D6:D7)')
    # worksheet_s.write(row, 14, total_costo, cell_total)
    # worksheet_s.write(row, 15, total_precio, cell_total)

    # close workbook
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data
