'''frutas=['tomate d arbol','maracuya','guayaba']
for f in frutas:
    print(f)
    if f == 'maracuya':
        break


fruits = ['manzana', 'banana', 'naranja']
for fruta in fruits:
    print(fruta)
'''
'''
for n in range(1,10):
    n=n+n
    print(n)
    n=n+n

for n in range(1,6):

    print(n)
'''
'''
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
'''
#sumeros pares desdendentes
'''
t=int(input("ingrese el numero desde el que desea que se calculen todos los pares en orden desendente "))
if(t%2==0):
    for i in range(t,1,-2):
        print (i)
elif(t%2!=0):
 t= t-1
for i in range(t,1,-2):
        print (i)
print('cambio de programa')

#imprimir numero y facrotial
t=int(input("ingrese el numero desde el que desea que se calculen todos los pares en orden desendente "))
t=t+1
for i in range(1,t):
    if(i ==1):
        print(f'el factorial de {i} =1')
    
    break
for i in range(2,t):
    f=i*(i-1)
    print(f'el factorial de {i} ={f}')
'''
def factorial(a):
    s=1
    for i in range(a,0,-1):
        s=s*i
    return s
print(factorial(3))


def maclaurina(x,n):
  i=0    

def ecponencial(x,n):
    for i in range(x,0):
        x**i

t=int(input('escriba el numero de grador que desea calcular'))
K=int(input('escriba el numero de del que se quiere calcular el elevado'))
t=t+1
for i in range(t,0):
    print(f'{K}^{t}')


