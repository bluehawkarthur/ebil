from django import template

register = template.Library()


def neto(total, ice, excentos, *args, **kwargs):
   
    return total - ice - excentos

register.simple_tag(neto)


def cf(total, ice, excentos, *args, **kwargs):
	neto = total - ice - excentos
	return neto * 13 / 100

register.simple_tag(cf)