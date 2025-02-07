for n in range(1,10):
    n=n+n
    print(n)
    n=n+n
print('fin')
for n in range(1,6):

    print(n)

#imprimir numero del 1 al 100
for n in range(1,101):
    print(n)
print ('cambio de programa')
#imprimir impares

for i in range(1,100,2):
    print (i)
print ('cambio de programa')

#imprimir pares
for i in range(2,101,2):
    print (i)
print ('cambio de programa')
#pares desendentes

t=int(input("ingrese el numero desde el que desea que se calculen todos los pares en orden desendente "))
if(t%2==0):
    for i in range(t,1,-2):
        print (i)
elif(t%2!=0):
 t= t-1
for i in range(t,1,-2):
        print (i)
print('cambio de programa')