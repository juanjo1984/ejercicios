# Ej1: 	Desarrolla una clase Cafetera con atributos _capacidadMaxima 
# 	(la cantidad máxima de café que puede contener la cafetera)
#  
# 	y _cantidadActual (la cantidad actual de café que hay en la 
# 	cafetera). Implementa, al menos, los siguientes métodos:
# 	Constructor predeterminado: establece la capacidad máxima en 
# 	1000 (c.c.) y la actual en cero (cafetera vacía).
	
# 	Constructor con la capacidad máxima de la cafetera; 
# 	inicializa la cantidad actual de café igual a la capacidad 
# 	máxima.

# 	Constructor con la capacidad máxima y la cantidad actual. 
# 	Si la cantidad actual es mayor que la capacidad máxima de 
# 	la cafetera, la ajustará al máximo.
# 	
# 	llenarCafetera(): pues eso, hace que la cantidad actual 
# 	sea igual a la capacidad.

# 	servirTaza(int): simula la acción de servir una taza 
# 	con la capacidad indicada.

# 	Si la cantidad actual de café “no alcanza” para llenar la 
# 	taza, se sirve lo que quede.

# 	vaciarCafetera(): pone la cantidad de café actual en cero.

# 	agregarCafe(int): añade a la cafetera la cantidad de café 
# 	indicada.

class Cafetera(object):
    
    def __init__(self, capacidad_maxima=1000, cantidad_actual=0):
        if  type(capacidad_maxima) not in (int, float):
            raise TypeError("ERROR AL CONSTRUIR EL OBJETO!! ==> CAPACIDAD MAXIMA NO ES UN NUMERO")
        if  type(cantidad_actual) not in (int, float):   
            raise TypeError("ERROR AL CONSTRUIR EL OBJETO!! ==> CANTIDAD ACTUAL")
        if cantidad_actual > capacidad_maxima:
            raise TypeError("ERROR AL CONSTRUIR EL OBJETO!! ==> CAPACIDAD MENOR A CANTIDAD ACTUAL")
        
        self.__capacidad_maxima = capacidad_maxima
        self.__cantidad_actual = cantidad_actual


    def vaciar_cafetera(self):
        pass
    def agregar_cafe(self,cantidad):
        pass
    def servirTaza(self,capacidad):
        pass
    def llenar_cafetera(self):
        pass

        


   

def main():
    c1 = Cafetera()
    c2 = Cafetera(555,0)
    c3 = Cafetera(capacidad_maxima = 2000)     
    c4 = Cafetera(cantidad_actual=100)
    c5 = Cafetera(cantidad_actual = 150,capacidad_maxima=1000)
    
    ok = False
    while not ok:
        try:
            a = int(input("ing: "))
            ok = True
        except  :
            print("INGRESE UN NUMERO ENTERO!!!! TYPE")
        # except ValueError :
        #     print("INGRESE UN NUMERO ENTERO!!!! VALUE")


if __name__ == "__main__":
    main()