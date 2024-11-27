"""#alrgotimo codigp ascii
##se pide un numero entero dentro den numero accii
print("ingrese un numero entero entre 1 y 255")
num = int(input("digite un numero entero:"))
##se hace un ciclo que eva
while ((num>= 1 and num<= 64) or (num>=91 and num<255)):
    s= chr(num)
    print("su simbolo es", s)
    print("ingrese un numero entero entre 1 y 255")
    num = int(input("digite un numero entero:"))
if (num >=65 and num<=90):
    print("su simbolo es una mayuscula")
elif(num<1 and num>255):
    print("el entero esta fuera de rango")

##funcion descuento5%"""
def f(x):
    return x*x

numcua =(input('ingrese el numero que desea al cuadrado'))
print(f(5))
##adhjshdjs