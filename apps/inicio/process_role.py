from apps.inicio.models import Rol


def rol(request):
    print 'processooooooooooo'

    roles = Rol.objects.filter(user=request.user.pk)
    item = {}
    clientes = {}
    proveedores = {}
    reportes = {}
    compras = {}
    usuarios = {}
    bancarizacion = {}
    configuracion = {}
    facturacion = {}

    for r in roles:
        if r.modelos == 'almacenes':
            item.update({
                'operar': r.operar,
                'crear': r.crear,
                'editar': r.editar,
                'eliminar': r.eliminar
            })

        if r.modelos == 'clientes':
            clientes.update({
                'operar': r.operar,
                'crear': r.crear,
                'editar': r.editar,
                'eliminar': r.eliminar
            })

        if r.modelos == 'proveedores':
            proveedores.update({
                'operar': r.operar,
                'crear': r.crear,
                'editar': r.editar,
                'eliminar': r.eliminar
            })

        if r.modelos == 'reportes':
            reportes.update({
                'operar': r.operar
            })

        if r.modelos == 'compras':
            compras.update({
                'operar': r.operar
            })

        if r.modelos == 'usuarios':
            usuarios.update({
                'operar': r.operar,
                'crear': r.crear,
                'editar': r.editar,
                'eliminar': r.eliminar
            })

        if r.modelos == 'bancarizacion':
            bancarizacion.update({
                'operar': r.operar
            })

        if r.modelos == 'configuracion':
            configuracion.update({
                'operar': r.operar
            })

        if r.modelos == 'facturacion':
            facturacion.update({
                'operar': r.operar
            })

    return {
        'almacenes_role': item,
        'clientes_role': clientes,
        'proveedores_role': proveedores,
        'reportes_role': reportes,
        'compras_role': compras,
        'usuarios_role': usuarios,
        'bancarizacion_role': bancarizacion,
        'configuracion_role': configuracion,
        'facturacion_role': facturacion,

    }
