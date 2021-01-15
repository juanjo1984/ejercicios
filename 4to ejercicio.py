from random import randint

LONGITUD = 8

def es_letra_mayuscula(caracter):
    return caracter >= 'A' and caracter <= 'Z'

def es_letra_minuscula(caracter):
    return caracter >= 'a' and caracter <= 'z'

def es_letra_digito(caracter):
    return caracter >= '0' and caracter <= '9'



def mayuscula_random():
    return chr(randint(ord('A'),ord('Z')))

def minuscula_random():
    return chr(randint(ord('a'),ord('z')))

def digito_random():
    return chr(randint(ord('0'),ord('9')))

class Password(object):
    
    def __init__(self,password=None,longitud=LONGITUD):
        if longitud < LONGITUD:
            self.__longitud = LONGITUD
        else:
            self.__longitud = longitud
        
        self.__password = self.__generar_password()
    
    
    
    def __generar_password(self):
        ok = False
        cadena = ""
        while not ok:
            cadena = ""
            for i in range(self.__longitud):
                n = randint(1,10)
                if n <= 7:
                    cadena += digito_random()
                elif n <= 9:
                    cadena += mayuscula_random()
                else:
                    cadena += minuscula_random()
            print(cadena)
            if self.__es_fuerte(cadena):
                ok=True
        return cadena    
    
    def __str__(self):
        return self.__password    
    
    def es_fuerte(self):
        return __es_fuerte(self.__password)
        
    
    def __es_fuerte(self, cadena):
        cma = 0
        cmi = 0
        cdi = 0
        for letra in cadena:
            if es_letra_mayuscula(letra):
                cma += 1
            elif es_letra_minuscula(letra):
                cmi += 1
            elif es_letra_digito(letra):
                cdi += 1
        return cma >= 2 and cmi >= 1 and cdi >= 5    
            
    
if __name__ == "__main__":
    pass    