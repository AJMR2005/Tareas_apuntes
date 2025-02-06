
valor = float(input("digite un numero real:"))
lista=[]
'''


#calcula el valor absoluto de x valor utilizando la funcion if
def valor_absoluto(x):
    if(x>=0):
        valora= x
    else:
        valora = -x
    return valora

print(f'el valor absoluto de {valor}= {valor_absoluto(valor)}')



#calculo de valor absoluto con el operador if ternario
def valor_tern(h):
    h if h>=0 else -h 
    return h
print(f'el valor absoluto de {valor}= {valor_tern(valor)}')


#impresion de numero con signo
def imp_num(x):
    if x>0:
        print(f'+ ', end="")
    print(x) 
    return x
imp_num(valor)
'''
'''
#determina si el primer caracter dentro de una cadena es par o no dentro del codigo ascii
cad=input(str('ingrese cadena de caracteres'))
for i in cad:
    lista.append(i)

cod=ord(lista[0])


if(cod%2)==0:
    char=chr(cod)
    c= print(f'{char} es par')
'''
'''
#programa que determina si dadas trees medidas se puede contruir un triangulo

a=int(input('ingrese la medida del primer lado'))
b=int(input('ingrese la medida del segundo lado'))
c=int(input('ingrese la medida del tercer lado'))


if (a+b)>c:
    print('con las medidas dadaas podemos relizar un triangulo')
    if(b+c)>a:
        print('con las medidas dadaas podemos relizar un triangulo')
    if(a+c)>b:
            print('con las medidas dadaas podemos relizar un triangulo')
else:
    print('con las medidas dadas no se ouede construir un triangulo')
'''


