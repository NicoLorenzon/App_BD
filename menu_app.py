'''
Esta clase será el menú de la aplicación.
Por medio del bloque while se generan las opciones a elegir por el usuario.
'''
from usuarioDAO import UsuarioDAO
from logg_base import log
from usuario import Usuario

opcion = None
while opcion != 5:
    print('Opciones')
    print('1- Lista de Usuarios') # SELECCIONAR
    print('2- Agregar un Usuario') # INSERTAR
    print('3- Actualizar usuario') # ACTUALIZAR
    print('4- Eliminar usuario') # ELIMINAR
    print('5- Salir') # SALIDA DE LA APP.

    opcion = int(input('Seleccione una opción: '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(f'{usuario}')

    elif opcion == 2:
        us_var = input('Usuario: ')
        ps_var = input('Contraseña: ')
        us_ag = Usuario(usuario = us_var, passw=ps_var)
        agregar = UsuarioDAO.insertar(us_ag)
        log.info('Usuario insertado con éxito!')

    elif opcion == 3:
        us_var = input('Nuevo username: ')
        ps_var = input('Nueva contraseña: ')
        ps_id = int(input('Ingrese su número de ID: '))
        us_act= Usuario(usuario= us_var, passw=ps_var, id_usuario=ps_id)
        actualizar = UsuarioDAO.actualizar(us_act)
        log.info('Usuario actualizado con éxito')

    elif opcion == 4:
        id_eli = int(input('Ingrese su número de ID a eliminar: '))
        us_eli = Usuario(id_usuario= id_eli)
        eliminar = UsuarioDAO.eliminar(us_eli)
        log.info('Usuario eliminado con éxito')

else:
    print('Salida del a app.')