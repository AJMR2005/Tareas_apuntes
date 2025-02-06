diccionario={}
datos_dic=int(input('ingrese la cantidad e elementos que desea agregar'))
for i in range(0,datos_dic+1):
    clave=input('ingrese clave')
    valor=input('ingrese valor')
    


a={123:"Rosa",87:'Rojas'}
b={"pruebaa":123, 123:"Rosa"}
#sentencia Try catch
print(a)

a[123]= 345
print(a)
try:
    print(a[10])
except:
    print('no se encuentra el elemento')