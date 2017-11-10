print "El Nombre del predefinido para el archivo Alumnos es : ( Alumnos )  "
print "El Nombre del predefinido para el archivo Salas es : ( Salas ) "

                ######      FUNCIONES      ######
                ######      FUNCIONES      ######


            #### FUNCIONES ALUMNOS ####

#Funcion que cuente los alumnos por ramo
#Entrada : El archivo de alumno que se quiere ingresar en comillas
#Salida : Cantidad de alumnos por el ramo "X" que se esta ingresando
def contador_dealumnosporramo(x):
    #Apertura del archivo
    listaAlumnos = open("Alumnos.txt")
    #se divide las lineas del texto en partes de una lista
    lineasdealumnos= listaAlumnos.readlines()
    ####contador ramos####
    # Establecemos una lista vacia para todos los ramos
    listaderamosgrande = []
    #contador sublista
    a = 0
    #Establecer una lista con solo los ramos
    while a < len(lineasdealumnos):
        # Apartamos la linea  en la cuan habra solo un alumno
        alumnoparticular = lineasdealumnos[a]
        # Declaramos una lista con la separacion de ","
        lalumnopar = alumnoparticular.split(",")
        # Contador que parte del primer ramo
        b = 1
        while b < (len(lalumnopar)- 1):
            # Agregamos a la lista de ramos los ramos del alumno
            listaderamosgrande.append(lalumnopar[b])
            b = b+1
        a =a+1
    contador = listaderamosgrande.count(x)
    listaAlumnos.close()
    return contador
#print contador_dealumnosporramo(Archivo)

#Funcion contador de elementos en una lista de otra lista **se utilizara para la funcion siguiente**
#Entrada : Elemento a contar, lista a recoorrer
#Salida : Las repeticiones del elemento en la lista
def contadorespecial(elemento,listarecorrer):
    c = 0
    while c<len(listarecorrer):
        cont = listarecorrer.count(elemento)
        c =c+1
    return cont
#print contadorespecial(P[i],Lista)

#Funcion que entrega los ramos ordenados por demanda
#Entrada : Archivo de alumnos y ramos "Alumnos.txt" ingresarlo por el nombre
#Salida : Lista de ramos ordenados por demanda
def ramos_ordenadospordemanda(x):
    #Apertura del archivo
    listaAlumnos = open(x)
    #se divide las lineas del texto en partes de una lista
    lineasdealumnos= listaAlumnos.readlines()
    #lista vacia para introducir todos los ramos del archivo en ella
    listaderamosgrande = []
    #contador sublista
    a = 0
    #Establecer una lista con solo los ramos
    while a < len(lineasdealumnos):
        # Apartamos la linea  en la cuan habra solo un alumno
        alumnoparticular = lineasdealumnos[a]
        # Declaramos una lista con la separacion de ","
        lalumnopar = alumnoparticular.split(",")
        # Contador que parte del primer ramo
        b = 1
        while b < (len(lalumnopar)- 1):
            # Agregamos a la lista de ramos los ramos del alumno
            listaderamosgrande.append(lalumnopar[b])
            b = b+1
        a =a+1
    #como tenemos cargados todos los ramos en la lista "listaderamosgrandes"
    #estableceremos una condicion para ordenar los ramos por cantidad, del mayor al menor
    #colocar ramos sin repeticiones
    Ramos = list(set(listaderamosgrande))

    #Lista con la cantidad de ramos por ramo respectivamente
    l = []
    s= 0
    while s < len(Ramos):
        repeticionderamo = contadorespecial(Ramos[s],listaderamosgrande)
        l.append(repeticionderamo)
        s= s+1
    #en una lista ponemos el ramo acompaÃƒÆ’Ã‚Â±ado de su cantidad de alumnos en un
    #sub indice de la lista
    lblanco =[]
    m = 0
    while m < len(Ramos):
        lblanco.append([l[m],Ramos[m]])
        m = m+1
    #ordenamos la lista de mayor a menor
    lblanco.sort(reverse = True)
    #Ciere del archivo
    listaAlumnos.close()
    Can=[]
    ra=[]
    p= 0
    while p < len(lblanco):
        Can.append(lblanco[p][0])
        ra.append(lblanco[p][1])
        p= p+1
    Listawena=[]
    Listawena.append(Can)
    Listawena.append(ra)

    return Listawena
#print ramos_ordenadospordemanda("Alumnos.txt")


                #### FUNCIONES SALAS ####

#Funcion
#Entrada : x = Archivo salas
#Salida : Lista Salas con bloques de horarios disponibles
def listadehorarios(x):
    #Se abre el archivo donde se encuentran las salas con sus horarios
    listaSalas=[]
    Archivo = open(x,"r")
    #iteramos para leer las lineas del archivo
    for horarios in Archivo:
        #generamos una lista separadas por las "," y eliminamos los saltos de linea del archivo
        lista=horarios.strip("\n").split(",")
        #iniciamos un contador en la lista creada
        i=1
        #iniciamos un iterador desde la posicion 1 donde se encuentran los horarios disponibles
        while i < len(lista):
            #aÃƒÆ’Ã‚Â±adimos a la listaSalas los bloques de horarios disponibles
            listaSalas.append([lista[i]])
            i+=1
    #cerramos el archivo
    Archivo.close()
    #regresamos la lista salas
    return listaSalas
####

#Funcion
#Entrada : una lista
#Salida : cantidad de separaciones en la lista ( cantidad de horarios)
def contadorhorarios(Lista):
    #iteramos la lista de horarios
    for listadentro in Lista:
        #iteramos la lista lista dentro de la lista, a esta le sacamos el largo que nos daria la cantidad
        #de horarios de una sala, al multiplicar este largo por el largo de la lista de todas las salas
        #obtenemos la cantidad total de bloques disponibles
        cantidadHorarios = (int(len(listadentro))*int(len(Lista)))
    return cantidadHorarios
####

#Funcion : crea el largo de la lista
#Entrada: archivosalas, cantidad de salas
#Salida: lista  apiladas donde indice = sala , lista dentro de lista = bloque disponible
def creacionlistaconbloquesdia(archivo,cantidadesalas) :
        matriz = []
        for i in range(cantidadesalas):
            matriz.append([])
            listasala= open(archivo)
            #se divide las lineas del texto en partes de una lista
            lineadesalas= listasala.readlines()
            #sublista de bloques de horario de una sala
            lis = lineadesalas[i]
            #eliminamos el saltodelinea y creamos la lista con separacionde ","
            Lgrande =lis.strip("\n").split(",")
            #columna para el vector de sala en bloques disponibles
            bloquedisponible = len(Lgrande)-1
            #se agrega en el rango de bloques disponibles de la sala
            for j in range(bloquedisponible):
                matriz[i].append("Bloquevacio")

        return matriz
####

                ##### FUNCIONES VARIAS #####

#para aproximar al entero por arriba math.ceil
import math

#Funcion Condicion que exista demanda
def peque(lista):
    peq = lista[0]
    a = peq.count(0)
    if a == len(lista[0]):
        valor = 0
    else:
        valor = 1
    return valor
##

#Cuenta bloques vacios disponibles
def horarioslibres(ListaHorario):
    a = 0
    p = 0
    while p< len(ListaHorario):
        b = ListaHorario[p].count("Bloquevacio")
        a = a+b
        p= p+1
        a
    return a
##

#Entrada
#Se solicita el nombre de los Archivos
#AAlumnos = raw_input("Ingrese el nombre del archivo Alumnos : ") + ".txt"
#ASalas = raw_input("Ingrese el nombre del Archivo Salas: ") + ".txt"
AAlumnos = "Alumnos.txt"
ASalas = "Salas.txt"
##Alumnos
#Se abre el archivo Alumnos
listaAlumnos = open(AAlumnos)
#Se divide las lineas del texto en partes de una lista
lineasdealumnos= listaAlumnos.readlines()
# Contador de alumnos totales
cantalumnos = len(lineasdealumnos)
listaAlumnos.close()
print "La cantidad de alumnos totales es : ", cantalumnos
##

##Salas
#Cantidas de bloques disponibles en Salas
Lista=listadehorarios(ASalas)
contador=contadorhorarios(Lista)
print "La cantidad de horarios disponibles es", contador,"\n"
##


                    ###### HEURISTICA 1 ######

## Alumnos
Alumnos = ramos_ordenadospordemanda(AAlumnos)
print "Los ramos que existen en la universidad, acompanado de su cantidad de alumnos : ", "\n",Alumnos, "\n"

## Salas
#Crear lista de Horario por un dia
listasala= open(ASalas)
lineadesalas= listasala.readlines()
#contar salas disponibles
Salasdisponibles = len(lineadesalas)
##HORARIO
#Como este horario se repite lunes, martes, miercoles, jueves, viernes, etc
#pedimos al usuario la cantidad de dias que el quiere utilizarlo para
#distribuir en esta lista los ramos
cantidadedias = input("Ingrese la cantidad de dias en la semana que abre la Universidad : ")
ListaHorario = creacionlistaconbloquesdia(ASalas,Salasdisponibles)

AlporSalas= input("Digite la cantidad de alumnos que cupen en una sala : ")

olumnos = Alumnos
cont = 0
while cont <len(olumnos[0]):
    olumnos[0][cont] = float(Alumnos[0][cont]) /AlporSalas
    cont = cont + 1
print "Los ramos que existen en la universidad, acompanado de su cantidad de bloques : ", "\n",olumnos, "\n"
def demanda(Alumnos):
    p =0
    B =0
    while p<len(Alumnos[0]):
        a = Alumnos[0][p]
        B = B+a
        p=p+1
    return B

def introducirramos(LHS,Alumnos):
    i = 0
    while i < len(LHS) :
        a = 0
        while a < len(LHS[i]):
            c = ganancia(Alumnos)
            if c == "No hay mas alumnos por asignar":
                LHS[i][a] = "Bloquevacio"

            elif c == "No hay mas bloques disponibles ":
                break
            else:
                LHS[i][a] = Alumnos[1][c]
                Alumnos[0][c]=Alumnos[0][c]-1
            a = a + 1
        i = i + 1
    return LHS
####
#funcion entrega lista cn ganancia de cada ramo
def ganancia(Alumnos):
    A = Alumnos
    totales = cantalumnos
    i = 0
    if peque(Alumnos) == 1:
        m = 0
        L= Alumnos[0]
        J= []
        while m < len(L):
            if cantalumnos <=0:
                w= "No hay mas alumnos por asignar"
                m = m+1
            elif demanda(Alumnos) <= 0:
                w= "No hay mas alumnos por asignar"
                m = m+1
            elif contador <= 0:

                w= "No hay mas bloques disponibles "
                m = m+1
            else:
                if Alumnos[0][m] < 0:
                    Alumnos[0][m] == 0

                a = (float(Alumnos[0][m])/cantalumnos)+(float(Alumnos[0][m])/demanda(Alumnos))+(float(horarioslibres(ListaHorario))/contador)
                J.append(a)
                m = m +1
                w = escojeelmaximo(J)

    return w
####

def escojeelmaximo(J):
    b= max(J)
    a = J.index(b)
    return a
####


#Creamos listas segun los dias de funcionamiento de la Universidad
L1 = ListaHorario
L2 = ListaHorario
L3 = ListaHorario
L4 = ListaHorario
L5 = ListaHorario
L6 = ListaHorario
L7 = ListaHorario

        ### PROCESAMIENTO ###

## Se introducen ramos dependiendo de la cantidad de dias que hay disponibles en la universidad##
if cantidadedias == 1:
    L1 = introducirramos(L1,olumnos)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    #Alumnos que sobran
    print olumnos

elif cantidadedias == 2:
    L1 = introducirramos(L1,olumnos)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,olumnos)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    #Alumnos que sobran
    print olumnos

elif cantidadedias == 3:
    L1 = introducirramos(L1,olumnos)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,olumnos)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,olumnos)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    #Alumnos que sobran
    print olumnos

elif cantidadedias == 4:
    L1 = introducirramos(L1,olumnos)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,olumnos)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,olumnos)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    L4 = introducirramos(L4,olumnos)
    print "\n","El Horario del dia Jueves para las salas es : ", "\n",L4,"\n"
    #Alumnos que sobran
    print olumnos

elif cantidadedias == 5:
    L1 = introducirramos(L1,olumnos)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,olumnos)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,olumnos)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    L4 = introducirramos(L4,olumnos)
    print "\n","El Horario del dia Jueves para las salas es : ", "\n",L4,"\n"
    L5 = introducirramos(L5,olumnos)
    print "\n","El Horario del dia Viernes para las salas es : ", "\n",L5,"\n"
    #Alumnos que sobran
    print olumnos

elif cantidadedias == 6:
    L1 = introducirramos(L1,olumnos)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,olumnos)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,olumnos)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    L4 = introducirramos(L4,olumnos)
    print "\n","El Horario del dia Jueves para las salas es : ", "\n",L4,"\n"
    L5 = introducirramos(L5,olumnos)
    print "\n","El Horario del dia Viernes para las salas es : ", "\n",L5,"\n"
    L6 = introducirramos(L6,olumnos)
    print "\n","El Horario del dia Sabado para las salas es : ", "\n",L6,"\n"
    #Alumnos que sobran
    print olumnos


elif cantidadedias == 7:
    L1 = introducirramos(L1,olumnos)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,olumnos)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,olumnos)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    L4 = introducirramos(L4,olumnos)
    print "\n","El Horario del dia Jueves para las salas es : ", "\n",L4,"\n"
    L5 = introducirramos(L5,olumnos)
    print "\n","El Horario del dia Viernes para las salas es : ", "\n",L5,"\n"
    L6 = introducirramos(L6,olumnos)
    print "\n","El Horario del dia Sabado para las salas es : ", "\n",L6,"\n"
    L7 = introducirramos(L7,olumnos)
    print "\n","El Horario del dia Domingo para las salas es : ", "\n",L7,"\n"
    #Alumnos que sobran
    print olumnos

elif cantidadedias <0 or cantidadedias > 7 or cantidadedias != int :
    print "Abra Nuevamente el programa entregando la informacion correctamente"
####
