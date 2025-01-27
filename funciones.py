def calcular_y(x:float,m:float,b:float)->float:
    return m*x+b

def test_linea():
    y = calcular_y(0,2.0,3.0)
    return y

if __name__ == '__main__':
    if test_linea()==3.0:
        print('Test Exitoso')
    else:
        print('Test Fallido')