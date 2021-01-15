Hacer una clase llamada Password que siga las siguientes condiciones:

Atributos:   

int    longitud 
String contraseña  

Por defectoa LONGITUD = 8

constructorese:
	Un constructor por defecto.
		Generara una contraseña aleatoria con LONGITUD
	Un constructor con la longitud que nosotros le pasemos. 
		Generara una contraseña aleatoria con esa longitud.

Los métodos que implementa serán:

esFuerte(): devuelve un booleano si es fuerte o no, para que sea 
	fuerte:
	2 o mas mayúsculas. 
	1 o mas minúsculas. 
	5 o mas digitos.

	8 ==> 100%

	5 ==>  70%
	2 ==>  20%
	1 ==>  10%

	n ==> [1,10] 

generarPassword():  genera la contraseña del objeto con la longitud que tenga.

Método get para contraseña y longitud.


'3' + '3' = '33'
3 + 3 = 6

int('3') + 3 = 6

str(5) + '5' = '55' 

ord('0') = 48
chr(48) = '0'

ord('A') = 65
chr(65) = 'A'