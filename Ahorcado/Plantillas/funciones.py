'''
Funciones auxiliares del juego Ahorcado
'''

def carga_archiv_texto(archivo : str) -> list:
    ''''
    Carga un archivo de texto y devuelve una lista con las oraciones del juego
    '''
    with open(archivo, 'r') as file:
        oraciones = file.readlines()
    return oraciones

if __name__ == '__main__':
    lista = carga_archiv_texto('./Plantillas/plantilla-0.txt')
    for elemento in lista:
        print(elemento)
