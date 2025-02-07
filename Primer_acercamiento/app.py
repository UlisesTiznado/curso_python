import argparse
import funciones

 
def main(m,b):
    
    # X =[x for x in range(1,11)]
    # Y =[funciones.Calcular_Y(x,m,b) for x in X]
    # print('Enteros:')
    # coordenadas_enteros = list(zip(X,Y))
    # print(coordenadas_enteros)
    X = [x/10.0 for x in range(10,110,5)]
    Y = [funciones.Calcular_Y(x,m,b) for x in X]
    coordenadas_flotantes = list(zip(X,Y))
    print('Flotantes')
    print(coordenadas_flotantes)
    funciones.grafica_linea(X,Y, m, b)



   
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=float,
                        help = 'Pendiente de la línea', default = 2.0)
    parser.add_argument('-b', type=float,
                        help='Ordenada al origen', default = 3.0)
    args= parser.parse_args()
    main(args.m, args.b)