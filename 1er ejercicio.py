#   DESARROLLO DEL PROGRAMA CON SUS CONSIGNAS SEPARADAS POR CADA ALGORITMO:

#   Ej:3	Crea una clase Fecha con atributos para el día, el mes y el año de la fecha. 
# 	Incluye, al menos, los siguientes métodos:
# 	Constructor predeterminado con el 1-1-1900 como fecha por defecto.
# 	Constructor parametrizado con día, mes y año.


class Fecha(object):
    # CONSTRUCTOR
    def __init__(self,dia=1,mes=1,anio=1900):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__meses = ("","Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio",
        "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    def get_dia(self):
        return self.__dia

    def set_dia(self,nombre):
        self.__dia = dia  

    def get_mes(self):
        return self.__mes

    def set_mes(self,mes):
        self.__mes = mes  

    def get_anio(self):
        return self.__anio

    def set_anio(self,anio):
        self.__anio = anio

    def el_nombre_del_mes(self):
        return self.__meses[self.__mes]

#   leer(): pedirá al usuario el día (1 a 31), el mes (1 a 12) y el año (1900 a 2050).

# 	bisiesto(): indicará si el año de la fecha es bisiesto o no.
    def esbisiesto(self):
        return self.__anio % 4 == 0 and self.__anio % 100 != 0 or self.__anio % 400 == 0
         
# 	diasMes(int): devolverá el número de días del mes que se le indique (para el año de la fecha).
    def diasMes(self):
        self.__dia = 31
        if self.__mes == 4 or self.__mes == 6 or self.__mes == 9 or self.__mes == 11:
            self.__dia == 30
        else:
            if self.__mes == 2:
                if esbisiesto(self.__anio):
                    self.__dia = 29
                else:
                    self.__dia = 28
        return self.__dia

#  	valida(): comprobará si la fecha es correcta (entre el 1-1-1900 y el 31-12-2050),si el día no es correcto,
#   lo pondrá a 1; si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900. 
#  	Será un método auxiliar (privado). Este método se llamará en el constructor parametrizado y en leer().
#  	Accedentes y mutadores.( get/set).
    def valida(self):
        pass

 # 	corta(): mostrará la fecha en formato corto (02-09-2003).
    def corta(self):
        return "{:02d}/{:02d}/{:4d}".format(self.dia,self.__mes,self.__anio)

#  	diasTranscurridos(): devolverá el número de días transcurridos desde el 1-1-1900 hasta la fecha.
    def dias_transcurridos(self):
        return ""

#  	diaSemana(): devolverá el día de la semana de la fecha(1 para domingo, ..., 7 para sábado).
#   El 1-1-1900 fue lunes.

    def diaSemana(self):
        dia = "Error"

        if self.__dia == 1:
            dia = "domingo"
        if self.__dia == 2:
            dia = "lunes"    
        if self.__dia == 3:
            dia = "martes"
        if self.__dia == 4:
            dia = "miercoles"
        if self.__dia == 5:
            dia = "jueves"
        if self.__dia == 6:
            dia = "viernes"
        if self.__dia == 7:
            dia = "sabado"

        return dia

#   larga(): mostrará la fecha en formato largo, empezando por el día de la semana(martes 2 de septiembre de 2003).

    def larga(self):
        return ""