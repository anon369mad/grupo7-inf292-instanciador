from instanciador import instanciacion, Instancia
import restricciones as req

def guardar_atributos_en_txt(instancia, nombre_archivo="atributos.txt"):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(restricciones.crear_funcion_objetivo(instancia.prioridad, instancia.num_asig))
        archivo.write(restricciones.crear_restriccion_interes(instancia.q_alumnos, instancia.cap_salas, instancia.num_asig))
        archivo.write(restricciones.crear_bloques_horarios_consecutivos(instancia.prioridad, instancia.h_restringidos, instancia.cap_salas, instancia.asig_bloques, instancia.num_asig, instancia.num_salas))
        archivo.write(restricciones.crear_asignacion_bloques(instancia.prioridad, instancia.cap_salas, instancia.asig_bloques, instancia.num_asig, instancia.num_salas))
        archivo.write(restricciones.crear_disponibilidad_asignatura(instancia.prioridad, instancia.cap_salas, instancia.num_asig, instancia.num_salas))
        archivo.write(restricciones.crear_tope_horario(instancia.prioridad, instancia.cap_salas, instancia.num_asig, instancia.num_salas))
        archivo.write(restricciones.crear_asignaturas_indispensables(instancia.prioridad, instancia.num_asig))

        # Horarios restringidos
        archivo.write("\\Horarios restringidos\n")
        for a, horarios in enumerate(instancia.h_restringidos):
            for h in horarios:
                for s in range(1, len(instancia.cap_salas) + 1):
                    archivo.write(f"x{a+1}_{s}_{h} = 0;\n")

        # Horarios disponibles
        '''archivo.write("\\Horarios Disponible\n")
        for a, horarios in enumerate(instancia.h_disponibles):
            print(instancia.h_disponibles)
            for h in horarios:
                for s in range(1, len(instancia.cap_salas) + 1):
                    archivo.write(f"x{a+1}_{s}_{h} <= 1;\n")'''

        # Variables binarias
        archivo.write("bin ")
        s = ", ".join(f"x{a}_{sala}_{h}" for a in range(1, len(instancia.prioridad) + 1)
                      for sala in range(1, len(instancia.cap_salas) + 1) for h in range(1, 36))
        archivo.write(s + ", ")

        # Variables y
        s = ", ".join(f"y{a}" for a in range(1, len(instancia.prioridad) + 1))
        archivo.write(s + ";\n")
        
flag=True
while flag:
 print("Elija una opción:")
 print("1-Generar instancia")
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
