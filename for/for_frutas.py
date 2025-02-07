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

'''
#sumer los pares desdendentes



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


