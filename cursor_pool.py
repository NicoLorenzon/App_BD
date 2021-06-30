'''
Este archivo va a genera el Cursor para poder interactuar con la base de datos
'''

from logg_base import log
from conexion import ConexionPool

class CursorDelPool:
    def __init__(self):
        '''
        Variables para utilizar la conexión y el cursor
        '''
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        '''
        El método enter genera la conexión y crea y devuelve el cursor
        '''
        log.debug('Inicio método enter')
        self._conexion = ConexionPool.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_execpcion, detalle_excepcion):
        '''
        Clase de manejo de errores, realiza un rollback en la acción y 
        devuelve mensaje detallando los errores.
        Si no se cometen errores realiza un commit de la acción realizada por el usuario.
        '''
        log.debug('Se ejecuta método __exit__')
        if valor_execpcion:
            self._conexion.rollback()
            log.error(f'Se produjo un error: {valor_execpcion}, {tipo_excepcion}, {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit en transacción realizado')
        '''Se cierra el cursor y se libera el pool'''
        self._cursor.close()
        ConexionPool.liberarPool(self._conexion)


if __name__ == '__main__':
    '''
    Bloque de prueba
    '''
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())