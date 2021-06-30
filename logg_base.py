'''
Manejo de errores a nivel debug.
'''

import logging as log

log.basicConfig(level= log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers =[log.FileHandler('capa-de-datos.log'),
                           log.StreamHandler()])
