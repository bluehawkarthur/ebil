from django import template


register = template.Library()


def neto(total, ice, excentos, *args, **kwargs):
   
    return total - ice - excentos

register.simple_tag(neto)


def cf(total, ice, excentos, *args, **kwargs):
	neto = total - ice - excentos
	return neto * 13 / 100

register.simple_tag(cf)

import datetime


def dias(fecha, *args, **kwargs):

	if fecha is None:
		day = 0
	else:
		today = datetime.date.today()
		day = (fecha-today).days
	
	return day

register.simple_tag(dias)
