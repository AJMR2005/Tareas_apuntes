#Arnold Joseph Merchan Rojas
#numero de arboles necesarios para obtener t numero de hojas
k=8
p=20
print('indique la cantidad de hojas que desea obtener')
t=int(input("Digite la cantiad de hojas "))
print(f'los arboles que necesitapodar para obtener{t} numero de hojases de')
A = (t)/k*p
print(f'{A} numero de arboles')

#interes
cant_dine = 0
dias = 0
interes = 0
int_sim =0
int_comp=0
cant_dine = int(input('ingrese la cantidad de dinero que le prestaron'))
dias=int(input('ingrese la cantidad de dias por la que le hicieron el prestamo'))
interes = int(input('ongrese el porcentaje de interes'))
int_sim= cant_dine=((cant_dine* interes)/100)

