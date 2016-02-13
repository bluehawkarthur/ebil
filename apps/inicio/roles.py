from rolepermissions.roles import AbstractUserRole


class Administrador(AbstractUserRole):
    available_permissions = {
        'create': True,
        'edit': True,
        'delete': True,

    }


class Operador(AbstractUserRole):
    available_permissions = {
        'edit': True,
    }
