# -*- coding: cp1252 -*-
# Distribucion de Horarios y Salas segun Demanda
# (Cesar Salazar - Benjamin Alcarruz- Penaa, 17.1114, 11-11-2017)

######      DEFINICION DE FUNCIONES      ######
######      DEFINICION DE FUNCIONES      ######

###############################################################################
#### FUNCIONES ALUMNOS ####
###############################################################################
# Funcion que cuente los alumnos por ramo
# Entrada : El archivo de alumno que se quiere ingresar en comillas
# Salida : Cantidad de alumnos por el ramo "X" que se esta ingresando
def contador_dealumnosporramo(x):
    # Apertura del archivo
    listaAlumnos = open(AAlumnos)
    # se divide las lineas del texto en partes de una lista
    lineasdealumnos = listaAlumnos.readlines()
    ####contador ramos####
    # Establecemos una lista vacia para todos los ramos
    listaderamosgrande = []
    # contador sublista
    a = 0
    # Establecer una lista con solo los ramos
    while a < len(lineasdealumnos):
        # Apartamos la linea  en la cuan habra solo un alumno
        alumnoparticular = lineasdealumnos[a]
        # Declaramos una lista con la separacion de ","
        lalumnopar = alumnoparticular.split(",")
        # Contador que parte del primer ramo
        b = 1
        while b < (len(lalumnopar) - 1):
            # Agregamos a la lista de ramos los ramos del alumno
            listaderamosgrande.append(lalumnopar[b])
            b = b + 1
        a = a + 1
    contador = listaderamosgrande.count(x)
    listaAlumnos.close()
    return contador
# print contador_dealumnosporramo(Archivo)


# Funcion contador de elementos en una lista de otra lista
# Entrada : Elemento a contar, lista a recoorrer
# Salida : Las repeticiones del elemento en la lista
def contadorespecial(elemento, listarecorrer):
    c = 0
    while c < len(listarecorrer):
        cont = listarecorrer.count(elemento)
        c = c + 1
    return cont
# print contadorespecial(P[i],Lista),**se utilizara para la funcion siguiente**


# Funcion que entrega los ramos ordenados por demanda
# Entrada : Archivo de alumnos y ramos "Alumnos.txt" ingresarlo por el nombre
# Salida : Lista de ramos ordenados por demanda
def ramos_ordenadospordemanda(x):
    # Apertura del archivo
    listaAlumnos = open(x)
    # se divide las lineas del texto en partes de una lista
    lineasdealumnos = listaAlumnos.readlines()
    # lista vacia para introducir todos los ramos del archivo en ella
    listaderamosgrande = []
    # contador sublista
    a = 0
    # Establecer una lista con solo los ramos
    while a < len(lineasdealumnos):
        # Apartamos la linea  en la cuan habra solo un alumno
        alumnoparticular = lineasdealumnos[a]
        # Declaramos una lista con la separacion de ","
        lalumnopar = alumnoparticular.split(",")
        # Contador que parte del primer ramo
        b = 1
        while b < (len(lalumnopar) - 1):
            # Agregamos a la lista de ramos los ramos del alumno
            listaderamosgrande.append(lalumnopar[b])
            b = b + 1
        a = a + 1
    # como tenemos cargados todos los ramos en la lista "listaderamosgrandes"
    # estableceremos una condicion para ordenar los ramos por cantidad, del mayor al menor
    # colocar ramos sin repeticiones
    Ramos = list(set(listaderamosgrande))
    # Lista con la cantidad de ramos por ramo respectivamente
    l = []
    s = 0
    while s < len(Ramos):
        repeticionderamo = contadorespecial(Ramos[s], listaderamosgrande)
        l.append(repeticionderamo)
        s = s + 1
    # en una lista ponemos el ramo acompaÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±ado de su cantidad de alumnos en un
    # sub indice de la lista
    lblanco = []
    m = 0
    while m < len(Ramos):
        lblanco.append([l[m], Ramos[m]])
        m = m + 1
    # ordenamos la lista de mayor a menor
    lblanco.sort(reverse=True)
    # Ciere del archivo
    listaAlumnos.close()
    Can = []
    ra = []
    p = 0
    while p < len(lblanco):
        Can.append(lblanco[p][0])
        ra.append(lblanco[p][1])
        p = p + 1
    Listawena = []
    Listawena.append(Can)
    Listawena.append(ra)
    return Listawena
# print ramos_ordenadospordemanda("Alumnos.txt")

###############################################################################
#### FUNCIONES SALAS ####
###############################################################################

# Funcion lista con bloques disponibles
# Entrada : Archivo salas
# Salida : Lista Salas con bloques de horarios disponibles
def listadehorarios(x):
    # Se abre el archivo donde se encuentran las salas con sus horarios
    listaSalas = []
    Archivo = open(x, "r")
    # iteramos para leer las lineas del archivo
    for horarios in Archivo:
        # generamos una lista separadas por las "," y eliminamos los saltos de linea del archivo
        lista = horarios.strip("\n").split(",")
        # iniciamos un contador en la lista creada
        i = 1
        # iniciamos un iterador desde la posicion 1 donde se encuentran los horarios disponibles
        while i < len(lista):
            # aÃƒÆ’Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â±adimos a la listaSalas los bloques de horarios disponibles
            listaSalas.append([lista[i]])
            i += 1
    # cerramos el archivo
    Archivo.close()
    # regresamos la lista salas
    return listaSalas
####

# Funcion cuenta horarios totales
# Entrada : una lista
# Salida : cantidad de separaciones en la lista ( cantidad de horarios)
def contadorhorarios(Lista):
    # iteramos la lista de horarios
    for listadentro in Lista:
        # iteramos la lista lista dentro de la lista, a esta le sacamos el largo que nos daria la cantidad
        # de horarios de una sala, al multiplicar este largo por el largo de la lista de todas las salas
        # obtenemos la cantidad total de bloques disponibles
        cantidadHorarios = (int(len(listadentro)) * int(len(Lista)))
    return cantidadHorarios
####

# Funcion : crea el largo de la lista
# Entrada: archivosalas, cantidad de salas
# Salida:lista apiladas donde indice=sala,lista dentro de lista=bloque disponible
def creacionlistaconbloquesdia(archivo, cantidadesalas):
    matriz = []
    for i in range(cantidadesalas):
        matriz.append([])
        listasala = open(archivo)
        # se divide las lineas del texto en partes de una lista
        lineadesalas = listasala.readlines()
        # sublista de bloques de horario de una sala
        lis = lineadesalas[i]
        # eliminamos el saltodelinea y creamos la lista con separacionde ","
        Lgrande = lis.strip("\n").split(",")
        # columna para el vector de sala en bloques disponibles
        bloquedisponible = len(Lgrande) - 1
        # se agrega en el rango de bloques disponibles de la sala
        for j in range(bloquedisponible):
            matriz[i].append("Bloquevacio")
    return matriz
####

###############################################################################
##### FUNCIONES VARIAS #####
###############################################################################

# Funcion verifica que exista demanda de ramos
# Entrada: lista con alumnos
# Salida: cantidad de bloques que se necesitan de ramos sin asignar
def bloquesquenecesita(Alumnos):
    p = 0
    B = 0
    while p < len(Alumnos[0]):
        a = Alumnos[0][p]
        if a > 0:
            B = B + a
        p = p + 1
    return B
####

# Funcion Condicion que exista demanda
# Entrada: lista con ramos y cantidad de salas
# Salida: 1 si hay demanda, 0 si no hay demanda
def existademanda(lista):
    peq = lista[0]
    n = 0
    #contador de ramos que no necesitan mas salas
    a = 0
    lv=[]
    while n<len(peq):
        if peq[n]<0:
            a = a+1
        n = n+1
    if a == len(lista[0]):
        valor = "No hay demanda"
    elif a < len(lista[0]):
        valor = "Si hay demanda"
    return valor
####

# Cuenta bloques vacios disponibles
# Entrada: lista horario del dia
# Salida: cantidad de horarios disponibles
def horarioslibres(ListaHorario):
    a = 0
    p = 0
    while p < len(ListaHorario):
        b = ListaHorario[p].count("Bloquevacio")
        a = a + b
        p = p + 1
    return a
####

# Funcion que introduce los ramos en bloques vacios
# Entrada:lista horario del dia , lista ramos con bloques
# Salida:lista horario con los ramos asignados
def introducirramos(LHS, Alumnos):
    i = 0
    while i < len(LHS):
        a = 0
        while a < len(LHS[i]):
            c = corroborar(Alumnos)
            if c == "No hay mas alumnos por asignar":
                LHS[i][a] = "--"
            elif c == "No hay mas bloques disponibles ":
                break
            elif c == "Go":
                o = 0
                while o < len(Alumnos[0]):
                    if Alumnos[0][o] < -1:
                        Alumnos[0][o] = 0
                    o = o + 1

                # Aplicacion de la restriccion
                L = Alumnos[0]
                J = []
                m = 0
                while m < len(L):
                    v = (float(Alumnos[0][m]) / cantalumnos) + (float(Alumnos[0][m]) / bloquesquenecesita(Alumnos)) + (
                    float(horarioslibres(ListaHorario)) / contador)
                    J.append(v)
                    m = m + 1

                c = escojeelmaximo(J)

                LHS[i][a] = Alumnos[1][c]
                #contiene lista con restricciones
                H = tiposderamos("Restriccion.txt")

                p = 0

                while p < len(H):
                    if LHS[i][a] in H[p]:

                        if LHS[i][a - 1] in H[p]:


                            for elemento in H[p]:
                                if elemento in Alumnos[1]:
                                    t= Alumnos[1]
                                    r= t.index(elemento)
                                    J[r]= 0


                    p = p + 1

                g = escojeelmaximo(J)

                LHS[i][a] = Alumnos[1][g]
                Alumnos[0][g] = Alumnos[0][g] - 1
            a = a + 1
        i = i + 1
    return LHS
####LHS=lista horario salas , Alumnos=lista con los ramos y bloques que necesita

# Funcion escoje el maximo
# Entrada: lista con ganancias
# Salida: indice del dato mas grande
def escojeelmaximo(J):
    b = max(J)
    a = J.index(b)
    return a
####

# Funcion extrae los tipos de ramos
# Entrada:archivo con lo#s tipos de ramos
# Salida:lista con cada sub indice con tipo de ramo
def tiposderamos(archivo):
    lista = open("Restriccion.txt")
    lineastipo = lista.readlines()
    # lista vacia para introducir todos los ramos del archivo en ella
    listatipo = []
    # contador sublista
    a = 0
    # Establecer una lista con solo los ramos
    while a < len(lineastipo):
        # Apartamos la linea  en la cuan habra solo un alumno
        tipoparticular = lineastipo[a]
        # Declaramos una lista con la separacion de ","
        tiparticular = tipoparticular.split(",")
        tiparticular.pop(0)
        tiparticular.pop(-1)
        listatipo.append(tiparticular)
        a = a + 1
    return listatipo
####

# Funcion entrega lista con ganancia de cada ramo
# Entrada: lista alumnos con bloques que necesita por ramo
# Salida: indice del ramo con la ganancia mas alta
def corroborar(Alumnos):
    A = Alumnos
    totales = cantalumnos
    i = 0
    if existademanda(Alumnos) == "Si hay demanda":
        m = 0
        L = Alumnos[0]
        if bloquesquenecesita(Alumnos) == 0:
            w = "No hay mas alumnos por asignar"
            m = m + 1
        else:
            w = "Go"

    elif existademanda(Alumnos) == "No hay demanda":
        w = "No hay mas alumnos por asignar"
    return w
####

#### Alumnos=lista con los ramos y bloques que necesita


# Funcion que calcula los alumnos que sobran
# Entrada Lista con bloques de ramos
# Salida lista con alumnos de ramos
def alumnosquesobran(Alummanejable):
    cont = 0
    while cont < len(Alummanejable[0]):
        Alummanejable[0][cont] = round((Alummanejable[0][cont]) * AlporSalas)
        cont = cont + 1
    return Alummanejable


#### Alummanejable = lista con los bloques sobrantes

###############################################################################
##############  BLOQUE PRINCIPAL ##############
##############  BLOQUE PRINCIPAL ##############
###############################################################################


print "El Nombre del predefinido para el archivo Alumnos es : ( Alumnos )  "
print "El Nombre del predefinido para el archivo Salas es : ( Salas ) "
print tiposderamos("Restriccion.txt")
# Alumnos
# Se solicita el nombre de los Archivos
AAlumnos = raw_input("Ingrese el nombre del archivo Alumnos : ") + ".txt"
ASalas = raw_input("Ingrese el nombre del Archivo Salas: ") + ".txt"

##Alumnos
# Se abre el archivo Alumnos
listaAlumnos = open(AAlumnos)
# Se divide las lineas del texto en partes de una lista
lineasdealumnos = listaAlumnos.readlines()
# Contador de alumnos totales
cantalumnos = len(lineasdealumnos)
listaAlumnos.close()
print "\n", "La cantidad de alumnos totales es : ", cantalumnos
##

##Salas
# Cantidas de bloques disponibles en Salas
Lista = listadehorarios(ASalas)
contador = contadorhorarios(Lista)
print "\n", "La cantidad de horarios disponibles es", contador, "\n"
##

## Alumnos por sala
AlporSalas = input("Digite la cantidad de alumnos que cupen en una sala : ")

###############################################################################
###### HEURISTICA con optimizacion ######
###############################################################################
### ENTRADAS ###
## Alumnos
Alumnos = ramos_ordenadospordemanda(AAlumnos)

## Salas
# Crear lista de Horario por un dia
listasala = open(ASalas)
lineadesalas = listasala.readlines()
# contar salas disponibles
Salasdisponibles = len(lineadesalas)

##HORARIO
# Se entrega un horario semanal para la universidad
ListaHorario = creacionlistaconbloquesdia(ASalas, Salasdisponibles)

### PROCESAMIENTO ###
print "Los ramos que existen en la universidad, acompanado de su cantidad de alumnos : ", "\n", Alumnos, "\n"
olumnos = Alumnos
## Se procesa los alumnos que requiere cada ramo a bloques de horario que requiere cada ramo
cont = 0
while cont < len(olumnos[0]):
    olumnos[0][cont] = round(float(Alumnos[0][cont]) / AlporSalas, 2)
    cont = cont + 1

print "Los ramos que existen en la universidad, acompanado de los bloques que necesitan : ", "\n", olumnos, "\n"
# Creamos listas segun los dias de funcionamiento de la Universidad
L1 = ListaHorario
L2 = ListaHorario
L3 = ListaHorario
L4 = ListaHorario
L5 = ListaHorario
L6 = ListaHorario
L7 = ListaHorario
###############################################################################
## Se introducen ramos dependiendo de la cantidad de dias que se seleccione ##
## Se ejecuta la funcion que introduce los ramos y luego se entrega al usuario##
###############################################################################
L1 = introducirramos(L1, olumnos)
print "\n", "El Horario del dia lunes para las salas es : ", "\n", L1, "\n"
L2 = introducirramos(L2, olumnos)
print "\n", "El Horario del dia Martes para las salas es : ", "\n", L2, "\n"
L3 = introducirramos(L3, olumnos)
print "\n", "El Horario del dia Miercoles para las salas es : ", "\n", L3, "\n"
L4 = introducirramos(L4, olumnos)
print "\n", "El Horario del dia Jueves para las salas es : ", "\n", L4, "\n"
L5 = introducirramos(L5, olumnos)
print "\n", "El Horario del dia Viernes para las salas es : ", "\n", L5, "\n"
L6 = introducirramos(L6, olumnos)
print "\n", "El Horario del dia Sabado para las salas es : ", "\n", L6, "\n"
L7 = introducirramos(L7, olumnos)
print "\n", "El Horario del dia Domingo para las salas es : ", "\n", L7, "\n"
# Alumnos que sobran
print "\n", "Los Alumnos que faltan por asignar en cada asignatura son : "
print "\n", alumnosquesobran(olumnos), "\n"

print "\n", "Considerar : Si los valores son negativos es porque sobran x asientos en la asignatura "
