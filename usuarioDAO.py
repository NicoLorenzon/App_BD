'''
Este archivo contiene el CRUD de usuario.
De este archivo se ejecutan las sentencias SQL según lo que el usuario
desee realizar, en la sección 
SELECCIONAR va a devolver una lista con los usuarios.
ACTUALIZAR Permite modificar el registro del usuario
INSERTAR Permite introducir un nuevo usuario
ELIMINAR Elimina el registro según el ID.
'''

from cursor_pool import CursorDelPool
from logg_base import log
from conexion import ConexionPool
from usuario import Usuario


class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _ACTUALIZAR = 'UPDATE usuario SET usuario=%s, passw=%s WHERE id_usuario = %s'
    _INSERTAR = 'INSERT INTO usuario (usuario, passw) VALUES(%s, %s)'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'


    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccion de usuarios')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            users = []
            for registro in registros:
                user = Usuario(registro[0], registro[1], registro[2])
                users.append(user)
            return users

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.usuario, usuario.passw, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona Actualizada {usuario}')
            return cursor.rowcount

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.usuario, usuario.passw)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado! {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario, )
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminado {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    '''
    Bloque de prueba
    '''
    persona1 = Usuario(id_usuario= None, usuario='XxXx',passw='2015')
    persona_insertada = UsuarioDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {persona_insertada}')


    usuario1 = Usuario(id_usuario=4)
    eliminar_us = UsuarioDAO.eliminar(usuario1)
    log.debug(f'Usuario Eliminado: {eliminar_us}')

    usuario2 = Usuario(usuario='XXXX', passw='Lala1', id_usuario=1)
    usuario_act = UsuarioDAO.actualizar(usuario2)
    log.debug(f'Usuario Actualizado: {usuario_act}')

    personas = UsuarioDAO.seleccionar()
    for persona in personas:
        log.debug(persona)