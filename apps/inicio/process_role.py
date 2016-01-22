from apps.inicio.models import Rol


def rol(request):
	print 'processooooooooooo'
	
	roles = Rol.objects.filter(user=request.user.pk)
	item = {}
	for r in roles:
		if r.modelos == 'almacenes':
			item.update({
				'crear':r.crear,
				'editar':r.editar,
				'eliminar':r.eliminar
			})
	print item
	return {
	'almacenes_role': item,
	}