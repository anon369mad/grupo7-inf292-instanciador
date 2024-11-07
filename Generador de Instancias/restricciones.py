# restricciones.py

def crear_funcion_objetivo(prioridad, num_asignaturas=1):
    f_o = "max: "
    for a in range(1, num_asignaturas + 1):
        f_o += f"{prioridad[a-1]} * y{a}+"
    return f_o[:-1] + ";\n"

def crear_restriccion_interes(q_alumnos, cap_salas, num_asignaturas=1):
    restriccion = "\\Interes\n"
    for a in range(1, num_asignaturas + 1):
        for capacity in cap_salas:
            restriccion += f"{q_alumnos[a-1]} <= {capacity} * y{a};\n"
    return restriccion

def crear_bloques_horarios_consecutivos(prioridad, h_restringidos, cap_salas, asig_bloques, num_asignaturas=1, num_salas=1):
    restriccion = "\\Bloques horarios consecutivos\n"
    for a in range(1, num_asignaturas + 1):
        for h in range(1, len(h_restringidos[a - 1]) + 1):
            for s in range(1, num_salas + 1):
                sum_expr = f"x{a}_{s}_{h}+x{a}_{s}_{h+1}="
                sum_expr += "2;\n" if a in asig_bloques else "1;\n"
                restriccion += sum_expr
    return restriccion

def crear_asignacion_bloques(prioridad, cap_salas, asig_bloques, num_asignaturas=1, num_salas=1):
    restriccion = "\\Asignación de bloques\n"
    for a in range(1, num_asignaturas + 1):
        sum_term = ""
        for h in range(1, 36):
            for s in range(1, num_salas + 1):
                sum_term += f"x{a}_{s}_{h} + "
        sum_term = sum_term[:-3] + " = " + ("2;\n" if a in asig_bloques else "1;\n")
        restriccion += sum_term
    return restriccion

def crear_disponibilidad_asignatura(prioridad, cap_salas, num_asignaturas=1, num_salas=1):
    restriccion = "\\Disponibilidad asignatura y Activación\n"
    for a in range(1, num_asignaturas + 1):
        sum_term = " + ".join(f"x{a}_{s}_{h}" for s in range(1, num_salas + 1) for h in range(1, 36))
        restriccion += f"y{a} <= {sum_term};\n"
    return restriccion

def crear_tope_horario(prioridad, cap_salas, num_asignaturas=1, num_salas=1):
    restriccion = "\\Tope de horario\n"
    for s in range(1, num_salas + 1):
        for h in range(1, 36):
            sum_term = " + ".join(f"x{a}_{s}_{h}" for a in range(1, num_asignaturas + 1))
            restriccion += f"{sum_term} <= 1;\n"
    return restriccion

def crear_asignaturas_indispensables(prioridad, num_asignaturas=1):
    restriccion = "\\Asignaturas Indispensables\n"
    for i in range(num_asignaturas):
        if prioridad[i] > 5:
            restriccion += f"y{i+1} = 1;\n"
    return restriccion