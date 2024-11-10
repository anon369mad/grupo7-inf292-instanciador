import random
#instancia pequeña: 1 sala 
#identificar cuántas asignaturas son necesarias para que la solución se vuelva infactible;  necesario generar al menos 5 instancias y analizar los resultados obtenidos.

class Instancia:
    def __init__(self, num_asig, num_salas):
        self.num_asig=num_asig
        self.num_salas=num_salas
        self.prioridad=f_prioridad(num_asig)
        self.h_disponibles=f_h_disponibles()
        self.h_restringidos=f_horarios_restringidos(num_asig, self.h_disponibles)
        self.cap_salas=f_cap_salas(num_salas)
        self.q_alumnos=f_q_alumnos(num_asig)
        self.asig_bloques=dar2bloquesalsesentaycincoporciento(num_asig)
        
        

#Prioridad de asignatura
def instanciacion():
    #instancias medianas
    q_asignaturas_medianas=[random.randint(30,35),random.randint(45,49), random.randint(60,64),random.randint(70,74), random.randint(80,84)]
    salas_medianas=[3,4,5,6,7]
    #instancias grandes
    q_asignaturas_grandes=[random.randint(140,160),random.randint(170,190), random.randint(200,220),random.randint(230,250), random.randint(280,300)]
    salas_grandes=[random.randint(10,12),random.randint(13,15),random.randint(16,18),random.randint(19,22),random.randint(23,25)]
    inst_medianas=[]
    inst_grandes=[]
    for i in range(0, 5):
        inst_medianas.append(Instancia(q_asignaturas_medianas[i], salas_medianas[i]))
        inst_grandes.append(Instancia(q_asignaturas_grandes[i], salas_grandes[i]))
    return inst_medianas, inst_grandes
    
#Retorna la proridad para a 
def f_prioridad(num_asignaturas): 
    num_asig_indispensable=num_asignaturas//5
    num_asig_no_indispensables=num_asignaturas-num_asig_indispensable
    lista_prioridad_indispensable=[random.randint(6, 10) for i in range(num_asig_indispensable)]
    lista_prioridad_no_indispensable=[random.randint(1, 5) for i in range(num_asig_no_indispensables)]
    lista_prioridades=lista_prioridad_indispensable+lista_prioridad_no_indispensable
    
    return lista_prioridades

#Retorna un array con arrays de los subindices-h (horarios) para subindices-a (asignaturas), en donde las asignaturas no pueden ser impartidas
def f_horarios_restringidos(num_asig, h_disponibles):
    h_restringidos_todos=[]
    for i in range(0, num_asig):
        qh_restringidos_profe=random.randint(7, 21)
        h_restringidos_profe = sorted(random.sample(h_disponibles, k=qh_restringidos_profe))
        h_restringidos_todos.append(h_restringidos_profe)
    return h_restringidos_todos

def f_cap_salas(num_salas):
    return [random.randint(45, 80) for i in range(num_salas)]

def f_q_alumnos(num_asig):
    return [random.randint(40, 80) for i in range(num_asig)]

#Retorna un array con los subindices-a (asignaturas) que tienen 2 bloques
def dar2bloquesalsesentaycincoporciento(num_asig):
    return sorted(random.sample(range(1, num_asig+1), k=(int(round(num_asig*0.65)))))
    
def f_h_disponibles():
    return sorted(random.sample(range(1, 36), k=35))
#instancia pequeña: 1 sala 
#identificar cuántas asignaturas son necesarias para que la solución se vuelva infactible;  necesario generar al menos 5 instancias y analizar los resultados obtenidos.