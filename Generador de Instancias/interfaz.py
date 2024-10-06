from instanciador import instanciacion, Instancia

def guardar_atributos_en_txt(instancia, nombre_archivo="atributos.txt"):
    with open(nombre_archivo, "w") as archivo:
        atributos = vars(instancia)  # Obtener todos los atributos de la instancia como un diccionario
        # Crear Función Objetivo
        a = 0
        f_o = ""
        archivo.write("MAXIMIZE\n")
        archivo.write("obj: ")
        for p_a in atributos["prioridad"]:
            f_o += f"{p_a} * y{a}+"
            a += 1
        f_o = f_o[:-1] + f_o[-1].replace("+", ";\n")
        archivo.write(f_o)

        # Crear restricciones
        # Interes
        archivo.write("SUBJECT TO\n")
        for interes in atributos["q_alumnos"]:
            for capacity in atributos["cap_salas"]:
                archivo.write(f"{interes} <= {capacity} * y{a};\n")
            a += 1
        # Horarios restringidos
        for a in range(1, len(atributos["h_restringidos"]) + 1):
            for h in range(1, len(atributos["h_restringidos"][a - 1]) + 1):
                for s in range(1, len(atributos["cap_salas"]) + 1):
                    archivo.write(f"x{a}_{s}_{h} = 0;\n")

        # Bloques horarios consecutivos
        sum = ""
        for a in range(1, len(atributos["prioridad"]) + 1):
            for h in range(1, len(atributos["h_restringidos"][a - 1]) + 1):
                for s in range(1, len(atributos["cap_salas"]) + 1):
                    sum += f"x{a}_{s}_{h} + x{a}_{s}_{h + 1} + "
            if a in atributos["asig_2bloques"]:
                sum = sum[:-1] + sum[-1].replace("+", "=2;\n")
            else:
                sum = sum[:-1] + sum[-1].replace("+", "=1;\n")
            archivo.write(sum)

        # Asignación de bloques
        sum = ""
        for a in range(1, len(atributos["prioridad"]) + 1):
            for h in range(1, len(atributos["h_restringidos"][a - 1]) + 1):
                for s in range(1, len(atributos["cap_salas"]) + 1):
                    sum += f"x{a}_{s}_{h} + "
            if a in atributos["asig_2bloques"]:
                sum = sum[:-1] + sum[-1].replace("+", "=2;\n")
            else:
                sum = sum[:-1] + sum[-1].replace("+", "=1;\n")
            archivo.write(sum)

        # Disponibilidad asignatura y Activación
        for a in range(1, len(atributos["prioridad"]) + 1):
            sum = ""
            for s in range(1, len(atributos["cap_salas"]) + 1):
                for h in range(1, 36):
                    sum += f"x{a}_{s}_{h} + "
            sum = f"y{a} <= " + sum[:-3] + ";\n"
            archivo.write(sum)

        # Tope de horario
        for s in range(1, len(atributos["cap_salas"]) + 1):
            for h in range(1, 36):
                sum = ""
                for a in range(1, len(atributos["prioridad"]) + 1):
                    sum += f"x{a}_{s}_{h} + "
                sum = sum[:-2] + "<= 1;\n"
                archivo.write(sum)

        # Asignaturas Indispensables
        x = 0
        for p_a in atributos["prioridad"]:
            if p_a > 5:
                archivo.write(f"y{x} = 1;\n")
            x += 1

        archivo.write("END")

        
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
