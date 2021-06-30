'''
Clase que genera el Usuario del cliente.
Se definen nombre de usuario y contraseña, ID se lo da automáticamente la BD.
Se generan métodos get y set para cada variable.
'''

from logg_base import log


class Usuario:
    def __init__(self, id_usuario=None, usuario=None, passw=None):
        self._id_usuario = id_usuario
        self._usuario = usuario
        self._passw = passw

    def __str__(self):
        return f'''
        ID: {self._id_usuario},
        User: {self._usuario},
        password: {self._passw}
        '''

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def passw(self):
        return self._passw

    @passw.setter
    def passw(self, passw):
        self._passw = passw


if __name__ == '__main__':
    '''
    Bloque de prueba
    '''
    user1 = Usuario(usuario='Nicolito', passw='312645')
    log.debug(user1)
    user2 = Usuario(usuario='Luzbelito', passw='Redondos')
    log.debug(user2)
