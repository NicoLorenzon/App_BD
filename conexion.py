'''
En este archivo se encuentran la clases que permiten la conexión con la base de datos,
los pools y sus funciones como obtener y liberar una vez que el usuario realiza la
transacción que desee.
'''

from psycopg2 import pool
from logg_base import log
import sys

class ConexionPool:
    '''
    Estas variables contienen los parámetros para lograr la conexion con la BD de Postgres
    '''
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST='127.0.0.1'
    _DB_PORT ='5432'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        '''
        Esta clase genera el pool y la conexión a la base de datos.
        Dentro del bloque try se encuentran los parámetros antes definidos, el bloque except
        si no es posible conectar devuelve el error y cierra la conexión.
        En El bloque else en caso de ya tener un pool creado lo llama y no se realiza uno nuevo.
        '''
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      user= cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      host= cls._HOST,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Se creó el pool correctamente')
                return cls._pool
            except Exception as e:
                print(f'Ocurrió un error al realizar el pool: {e}')
                sys.exit()

        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        '''
        Con esta función obtenemos la conexión con la BD,
        automáticamente nos genera el pool
        '''
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida desde el pool. {conexion}')
        return conexion

    @classmethod
    def liberarPool(cls, conexion):
        '''
        En esta función se liberan los pool, es decir que cada vez que un pool termine de ejecutar se libera
        un espacio para una nueva consulta dentro del programa. Se devuelve el mensaje para corroborarlo.
        '''
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Se liberó el pool. {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        '''Acá se van a cerrar todas las conexiones'''
        cls.obtenerPool().closeall()
        log.debug('Conexiones del pool Cerradas')

if __name__ == '__main__':
    '''
    Bloque de prueba
    '''
    conexion1= ConexionPool.obtenerConexion()
    ConexionPool.liberarPool(conexion1)
    conexion2 = ConexionPool.obtenerConexion()
    ConexionPool.cerrarConexiones()