#Imports
import os #Importa el simbolo de sistema

#Funciones
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#Inicializo variables
dir = [] #Almacena los archivos y carpetas
path = os.getcwd() #Almacena la direccion
order = '' #Almacena el comando

################
####Programa####
################

#Navegacion de directorios
while (order!='END'):
	dir = os.listdir(path)
	print 'Estas en ' + path
	print ''
	print 'COMMANDS: GO / END'
	print ''
	for x in dir:
		print x
	print ''
	order = str(raw_input("Orden: ")).upper()
	if order[:7] == 'GO BACK':
		os.chdir('..')
	elif order[:2] == 'GO':
		os.chdir('./'+order[3:])
	path = os.getcwd()
	dir = []

#Elector de parametros
print'Parametro de eleccion:'
print ''
print '-c Carpetas' #p1
print '-a Archivos' #p1 // todos #p2
print 'nom-- Que comience con nom'
print '--nom Que termine con nom'
print '--nom-- Que contenga nom'
print '! Negador' #p3
print ''
parametro = str(raw_input("Parametro: "))

#Condiciona la seleccion de archivos y carpetas
p1=False
p2=False
p3=False
if '-c' in parametro:
	p1=False
elif '-a' in parametro:
	p1=True
elif '*' in parametro:
	p3=True

dir = [x for x in os.listdir(path) if (os.path.isdir(x) != p1) or p2]
print dir

#Elector de cambios
print ''
print 'Cambios y condiciones:'
print ''
print '*nnom Agregar al final'
print '/5 elimina los primeros 5 caracteres'
print '5/ elimina los ultimos 5 caracteres'
print 'nnom* Agregar al principio'
print ''
comando = str(raw_input("Comando: "))

borrar= ''
cont=0
primero = 0
if '/' in comando:
	if comando[0] == '/':
		cont=1
		primero = 1
	else:
		primero = 2
	while(is_number(comando[cont])):
			borrar+=comando[cont]
			cont+=1
	print 'borrar: ' + borrar
	cont=2

cont2=0
for folder in dir:	#Realiza los cambios
	cont2+=1
	if len(comando) > (len(borrar)+cont):
		if primero == 1:
			if comando[len(borrar)+cont]=='*':
				os.rename(folder,folder[int(borrar):] + comando[len(borrar)+cont+1:])
			elif comando[len(comando)-1]=='*':
				os.rename(folder,comando[len(borrar)+cont:len(comando)-1] + folder[int(borrar):])
			else:
				os.rename(folder,comando + str(cont2))
		elif primero == 2:
			if comando[len(borrar)+cont]=='*':
				os.rename(folder,folder[:len(folder)-int(borrar)] + comando[len(borrar)+cont+1:])
			elif comando[len(comando)-1]=='*':
				os.rename(folder,comando[len(borrar)+cont:len(comando)-1] + folder[:len(folder)-int(borrar)] )
			else:
				os.rename(folder,comando + str(cont2))
		elif primero == 0:
			if comando[len(borrar)+cont]=='*':
				os.rename(folder,folder + comando[len(borrar)+cont+1:])
			elif comando[len(comando)-1]=='*':
				os.rename(folder,comando[len(borrar)+cont:len(comando)-1] + folder)
			else:
				os.rename(folder,comando + str(cont2))
	else:
		if primero==1:
			os.rename(folder,folder[int(borrar):])
		elif primero==2:
			os.rename(folder,folder[:len(folder)-int(borrar)])
			
			