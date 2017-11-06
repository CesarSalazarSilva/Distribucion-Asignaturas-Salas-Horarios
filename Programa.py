print "El Nombre del predefinido para el archivo Alumnos es : ( Alumnos )  "
print "El Nombre del predefinido para el archivo Salas es : ( Salas ) "

                ######      FUNCIONES      ######
                ######      FUNCIONES      ######


            #### MANEJO CONTADOR DE ALUMNOS ####
#para aproximar al entero por arriba math.ceil
import math

#Funcion verifica que exista un 0 en la posicion si es asi aumenta en 1 el contador
#Entrada:Lista a verificar
#Salida: indice necesario para el proceso
def verifico(Alummanejable):
    i = 0
    p = 0
    while p > -1:
        if Alummanejable[p][0]== 0:
            p= p +1
            if Alummanejable[len(Alummanejable)-1][0]==0:
                i = -1
                p = -3
        elif Alummanejable[p][0] != 0:
            i=p
            p=-3
    return i

#Funcionintroduce el ramo en el bloque vacio
#Entrada lista de Salas y alumnos
#Salida lista salas con los ramos asignados
def introducirramos(LHS,Alummanejable):
    i = 0
    while i < len(LHS) :
        a = 0
        while a < len(LHS[i]):
            c = verifico(Alummanejable)
            if c == -1:
                LHS[i][a] = "BloqueVacio"
            elif c != -1 :
                LHS[i][a] = Alummanejable[c][1]
                Alummanejable[c][0]=Alummanejable[c][0]-1
            a = a + 1
        i = i + 1
    return LHS

#Funcion Contador especial para asignar Ramos en salas
#Entrada: lista a verificar
#Salida: indice de la lista ramos a asignar en lista sala
def verifica(lista):
    cont = 0
    o = 0
    while o > -1 :
        if lista[o][0] == 0:
            con = con + 1
            o = o + 1

        elif lista[o][0] < len(lista):
            cont = cont +1
            o = -1
        elif lista[o][0] == len(lista):
            o = 0

    return cont

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
    #en una lista ponemos el ramo acompaÃƒÂ±ado de su cantidad de alumnos en un
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

    return lblanco
#print ramos_ordenadospordemanda("Alumnos.txt")


            #### MANEJO DE BLOQUES SALAS ####

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
            #aÃƒÂ±adimos a la listaSalas los bloques de horarios disponibles
            listaSalas.append([lista[i]])
            i+=1
    #cerramos el archivo
    Archivo.close()
    #regresamos la lista salas
    return listaSalas

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

                ########## Procesamiento ##########


                ####### Bloque Principal ########

#entrada
#El nombre de los archivos queda
AAlumnos = raw_input("Ingrese el nombre del archivo Alumnos : ") + ".txt"
ASalas = raw_input("Ingrese el nombre del Archivo Salas: ") + ".txt"


listaAlumnos = open(AAlumnos)
#Procesamiento
#Se divide las lineas del texto en partes de una lista
lineasdealumnos= listaAlumnos.readlines()
# Contador de alumnos totales
cantalumnos = len(lineasdealumnos)
listaAlumnos.close()
#Salida
#print "La cantidad de alumnos totales es : ", cantalumnos


#Cantidas de bloques disponibles en Salas
#Procesamiento
Lista=listadehorarios(ASalas)
contador=contadorhorarios(Lista)
#Salida
print "la cantidad de horarios disponibles es", contador,"\n"




                    ###### HEURISTICA 1 ######

    ## Alumnos
Alumnos = ramos_ordenadospordemanda(AAlumnos)
print "Los ramos que existen en la universidad, acompanado de su cantidad de alumnos : ", "\n",Alumnos

    ## Salas
#Crear lista de Horario por un dia
listasala= open(ASalas)
lineadesalas= listasala.readlines()
#contar salas disponibles
Salasdisponibles = len(lineadesalas)

# Como este horario se repite lunes, martes, miercoles, jueves, viernes, etc
#pedimos al usuario la cantidad de dias que el quiere utilizarlo para
#distribuir en esta lista los ramos
cantidadedias = input("Ingrese la cantidad de dias en la semana que abre la Universidad : ")

#ingresar el nombre del archivo para utilizarlo en la funcion
#horario indice = sala, listo dentro de lista = bloques de horarios
ListaHorario = creacionlistaconbloquesdia(ASalas,Salasdisponibles)


L1 = ListaHorario
L2 = ListaHorario
L3 = ListaHorario
L4 = ListaHorario
L5 = ListaHorario
L6 = ListaHorario
L7 = ListaHorario

# funcion que entrega los alumnos que no alcanzaron a quedar
# Entrada:Lista bbloques de ramos que sobran
# Salida:lista con alumnos que faltan por asignar
def alumnosquesobran(Alummanejable,Al):
    cont = 0
    while cont<len(Alummanejable):
        if Alummanejable[cont][0] == 0:
            cont = cont +1
        else:
            a=(math.ceil(float(alumnos[cont][0]) /AlporSalas))-(float(alumnos[cont][0]) /AlporSalas)
            Alummanejable[cont][0] = (Alummanejable[cont][0] - a)*AlporSalas
            cont = cont + 1

    return Alummanejable

AlporSalas = input("Introduzca la cantidad de alumnos que cupen en una sala : ")
#Se crea una lista para utilizar la funcion alumnos que sobran
Al = Alumnos
#se crea una lista con el fin de cambiar el indice en vez de alumnos a salas a solicitar
Alummanejable = Alumnos
#se divide la cantidad de alumnos en en ramo por la cantidad de alumnos por sala se da cuantos bloques necesita el ramo
cont = 0
while cont <len(Alummanejable):
    Alummanejable[cont][0] = math.ceil(float(Alummanejable[cont][0]) /AlporSalas)
    cont = cont + 1


if cantidadedias == 1:
    L1 = introducirramos(L1,Alummanejable)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    #Alumnos que sobran
    Alsob = alumnosquesobran(Alummanejable,Al)
    print Alsob

elif cantidadedias == 2:
    L1 = introducirramos(L1,Alummanejable)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,Alummanejable)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    #Alumnos que sobran
    Alsob = alumnosquesobran(Alummanejable,Al)
    print Alsob


elif cantidadedias == 3:
    L1 = introducirramos(L1,Alummanejable)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,Alummanejable)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,Alummanejable)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    #Alumnos que sobran
    Alsob = alumnosquesobran(Alummanejable,Al)
    print Alsob

elif cantidadedias == 4:
    L1 = introducirramos(L1,Alummanejable)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,Alummanejable)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,Alummanejable)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    L4 = introducirramos(L4,Alummanejable)
    print "\n","El Horario del dia Jueves para las salas es : ", "\n",L4,"\n"
    #Alumnos que sobran
    Alsob = alumnosquesobran(Alummanejable,Al)
    print Alsob

elif cantidadedias == 5:
    L1 = introducirramos(L1,Alummanejable)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,Alummanejable)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,Alummanejable)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    L4 = introducirramos(L4,Alummanejable)
    print "\n","El Horario del dia Jueves para las salas es : ", "\n",L4,"\n"
    L5 = introducirramos(L5,Alummanejable)
    print "\n","El Horario del dia Viernes para las salas es : ", "\n",L5,"\n"
    #Alumnos que sobran
    Alsob = alumnosquesobran(Alummanejable,Al)
    print Alsob

elif cantidadedias == 6:
    L1 = introducirramos(L1,Alummanejable)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,Alummanejable)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,Alummanejable)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    L4 = introducirramos(L4,Alummanejable)
    print "\n","El Horario del dia Jueves para las salas es : ", "\n",L4,"\n"
    L5 = introducirramos(L5,Alummanejable)
    print "\n","El Horario del dia Viernes para las salas es : ", "\n",L5,"\n"
    L6 = introducirramos(L6,Alummanejable)
    print "\n","El Horario del dia Sabado para las salas es : ", "\n",L6,"\n"
    #Alumnos que sobran
    Alsob = alumnosquesobran(Alummanejable,Al)
    print Alsob

elif cantidadedias == 7:
    L1 = introducirramos(L1,Alummanejable)
    print "\n","El Horario del dia lunes para las salas es : ", "\n",L1,"\n"
    L2 = introducirramos(L2,Alummanejable)
    print "\n","El Horario del dia Martes para las salas es : ", "\n",L2,"\n"
    L3 = introducirramos(L3,Alummanejable)
    print "\n","El Horario del dia Miercoles para las salas es : ", "\n",L3,"\n"
    L4 = introducirramos(L4,Alummanejable)
    print "\n","El Horario del dia Jueves para las salas es : ", "\n",L4,"\n"
    L5 = introducirramos(L5,Alummanejable)
    print "\n","El Horario del dia Viernes para las salas es : ", "\n",L5,"\n"
    L6 = introducirramos(L6,Alummanejable)
    print "\n","El Horario del dia Sabado para las salas es : ", "\n",L6,"\n"
    L7 = introducirramos(L7,Alummanejable)
    print "\n","El Horario del dia Domingo para las salas es : ", "\n",L7,"\n"
    #Alumnos que sobran
    Alsob = alumnosquesobran(Alummanejable,Al)
    print Alsob

elif cantidadedias <0 or cantidadedias > 7 or cantidadedias != int :
    print "Abra Nuevamente el programa entregando la informacion correctamente"



                    ###### HEURISTICA 2 ######
                        #### Alg.voraz ####




