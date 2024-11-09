# restricciones.py

def crear_funcion_objetivo(prioridad, num_asignaturas=1):
    f_o = "max: "
    for a in range(1, num_asignaturas + 1):
        f_o += f"{prioridad[a-1]} * y{a}+"
    return f_o[:-1] + ";\n"

def crear_restriccion_interes(q_alumnos, cap_salas, num_asignaturas=1, num_salas=1):
    restriccion = "/* R1 - Capacidad de las salas de clases (Interés) */\n"
    for a in range(1, num_asignaturas + 1):
        for s, capacity in enumerate(cap_salas):
            sum_expr = ""
            for h in range(1, 71):
                sum_expr += f"{q_alumnos[a-1]} x{a}_{s}_{h}"
                sum_expr += " + " if h < 70 else f" <= {capacity};\n"
            restriccion += sum_expr
    return restriccion

def crear_bloques_horarios_consecutivos(prioridad, h_restringidos, cap_salas, asig_bloques, num_asignaturas=1, num_salas=1):
    restriccion = "/* R2 - Bloques horarios consecutivos */\n"
    for a in range(1, num_asignaturas + 1):
        for h in range(1, len(h_restringidos[a - 1]) + 1):
            for s in range(1, num_salas + 1):
                if a in asig_bloques:
                    sum_expr = f"x{a}_{s}_{h-1}+x{a}_{s}_{h+1}+x{a}_{s}_{h}="
                    sum_expr += f"2*x{a}_{s}_{h};\n" 
                restriccion += sum_expr
    return restriccion

def crear_asignacion_bloques(prioridad, cap_salas, asig_bloques, num_asignaturas=1, num_salas=1):
    restriccion = "/* R3 - Asignación de bloques */\n"
    for a in range(1, num_asignaturas + 1):
        sum_term = ""
        for h in range(1, 36):
            for s in range(1, num_salas + 1):
                sum_term += f"x{a}_{s}_{h} + "
        sum_term = sum_term[:-3] + " = " + ("2;\n" if a in asig_bloques else "1;\n")
        restriccion += sum_term
    return restriccion

def crear_disponibilidad_asignatura(prioridad, cap_salas, num_asignaturas=1, num_salas=1):
    restriccion = "/* R4 - Disponibilidad asignatura y Activación */\n"
    for a in range(1, num_asignaturas + 1):
        sum_term = " + ".join(f"x{a}_{s}_{h}" for s in range(1, num_salas + 1) for h in range(1, 36))
        restriccion += f"y{a} <= {sum_term};\n"
    return restriccion

def crear_tope_horario(num_asignaturas=1, num_salas=1):
    restriccion = "/* R6 - Tope de horario */\n"
    for s in range(1, num_salas + 1):
        for h in range(1, 36):
            sum_term = " + ".join(f"x{a}_{s}_{h}" for a in range(1, num_asignaturas + 1))
            restriccion += f"{sum_term} <= 1;\n"
    return restriccion

def crear_asignaturas_indispensables(prioridad, num_asignaturas=1):
    restriccion = "/* R7 - Asignaturas Indispensables */\n"
    for i in range(num_asignaturas):
        if prioridad[i] > 5:
            restriccion += f"y{i+1} = 1;\n"
    return restriccion
