from instanciador import instanciacion, Instancia

def guardar_atributos_en_txt(instancia, nombre_archivo="atributos.txt"):
    with open(nombre_archivo, "w") as archivo:
        atributos = vars(instancia)  # Obtener todos los atributos de la instancia como un diccionario
        for atributo, valor in atributos.items():
            archivo.write(f"{atributo}: {valor}\n")
flag=True
while flag:
 print("Elija una opción:")
 print("1-Generar instancia pequeña")
 print("2-Generar 5 instancias medianas y 5 grandes")
 print("0-Salir")
 opcion=int(input())
 
 if opcion==1:
  print("¿Número de asignaturas?")
  instancia=Instancia(int(input()), 1)
  guardar_atributos_en_txt(instancia, "InstanciaP.txt")
  print("Archivos con instancias creados")
 
 if opcion==2:
  inst_m, inst_g = instanciacion()
  for i in range(0, 5):
   guardar_atributos_en_txt(inst_m[i], "InstanciaM"+i+".txt")
   guardar_atributos_en_txt(inst_g[i], "InstanciaG"+i+".txt")
   print("Archivos con instancias creados")
 
 if opcion==0:
  flag=False
  print("Bye bye")
