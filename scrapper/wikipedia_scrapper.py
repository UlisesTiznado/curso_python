import os
import argparse
import 


def scrap(url:str):
    '''Obtiene página desde Internet'''
    pagina = request.get(url)


    def guardar_pagina(pagina,nombre_archivo: str):
        '''Guarda la pagina en un archivo'''
        with open(nombre_archivo, 'wb') as f:
            f.write(pagina.contetn)
            