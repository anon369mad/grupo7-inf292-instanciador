from instanciador import instanciacion, Instancia

def guardar_atributos_en_txt(instancia, nombre_archivo="atributos.txt"):
    with open(nombre_archivo, "w") as archivo:
        atributos = vars(instancia)  # Obtener todos los atributos de la instancia como un diccionario
        #Crear Función Objetivo
        a=0
        for p_a in atributo[prioridad]):
            archivo.write(f"{p_a} y",a,"+")
            a+=1
flag=True
while flag:
 print("Elija una opción:")
 print("1-Generar instancia pequeña")
 print("2-Generar 5 instancias medianas y 5 grandes")
 print("0-Salir")
 opcion=int(input())
 
 if opcion==1:
  print("¿Número de asignaturas?")
  num_asig=int(input())
  print("¿Número de salas?")
  num_salas=int(input())
  instancia=Instancia(num_asig, num_salas)
  guardar_atributos_en_txt(instancia, "InstanciaP.txt")
  print("Archivos con instancias creados")
 
 if opcion==0:
  flag=False
  print("Bye bye")
