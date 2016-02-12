from apps.inicio.models import Rol


def rol(request):
	print 'processooooooooooo'
	
	roles = Rol.objects.filter(user=request.user.pk)
	item = {}
	clientes = {}
	for r in roles:
		if r.modelos == 'almacenes':
			item.update({
				'operar':r.operar,
				'crear':r.crear,
				'editar':r.editar,
				'eliminar':r.eliminar
			})

		if r.modelos == 'clientes':
			clientes.update({
				'operar':r.operar,
				'crear':r.crear,
				'editar':r.editar,
				'eliminar':r.eliminar
			})

	print item
	return {
	'almacenes_role': item,
	'clientes_role': clientes,
	}