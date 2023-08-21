# Kata de hoy - String Calculator

## Primer parte 
int Sumar(string numeros)
———————————————

El método puede tomar uno, dos números enteros o más, separados por coma. 

Un string vacío suma 0.

Ejemplos: “1,2”=3 “4,2”=6 “”=0 “3,8,7”=18

Piensan un primer test que les sirva para conducir la implementación de este metodo.

1. Ejecutan el Test (deberia darles rojo) - RED
2. Escriben la implementación mas sencilla que logre que ese Test pase (debaria darles verde) - GREEN
3. Revisan la calidad del çodigo, si hace falta hacen cambios y vuelve a ejecutar el Test para asegurarse que todo esta bien. -  REFACTOR (BLUE)

Luego de eso, si la funcionalidad todavia no esta lista, eligen otro test y repiten el ciclo.

## Segunda parte

También admite nuevas líneas, o sea, que venga el caracter separador de line en el texto: “\n”

Ejemplo: “1,2,4\n5,6”=18 

## Tercer parte

El delimitador es configurable si se agrega //[delimitador]\n al principio.

Ejemplo: “//;\n1;3;6;4”=14
Ejemplo: “//|\n1|3|6|4”=14

O sea, en lugar que el delimitador sea siempre "," que seria el default, se puede configurar que se use otro aclarandolo al arranque del string de la forma que muestran los ejemplos.