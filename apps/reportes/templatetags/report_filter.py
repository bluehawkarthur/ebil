# -*- coding: utf-8 -*-
from django import template
from apps.reportes.num2word.num2word_ES import to_card, to_ord, to_ordnum

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


def resta(num1, mun2, *args, **kwargs):
	total = 0
	if mun2 is None:
		mun2 = 0
		total = num1
	else:
		total = num1 - mun2
	return total

register.simple_tag(resta)


def texto(num, *args, **kwargs):

	num1 = str(num)

	num2 = num1.split('.')
	
	text = to_card(int(num))
	text_final = '%s %s/%s' % (text, num2[1], '100')
	
	return text_final.upper()

register.simple_tag(texto)


@register.filter(name='range')
def _range(_min, args=None):
    _max, _step = None, None
    if args:
        if not isinstance(args, int):
            _max, _step = map(int, args.split(','))
        else:
            _max = args
    args = filter(None, (_min - _max, _max, _step))
    return range(*args)
