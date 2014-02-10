#Imports
import os #Importa el simbolo de sistema

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
print '-c Carpetas'
print '-a Archivos'
print '--all Todos'
print 'nom-- Que comience con nom'
print '--nom Que termine con nom'
print '--nom-- Que contenga nom'
print ''
parametro = str(raw_input("Parametro: "))


	
	
#path = r'C:\Users\Ramiro\Desktop\Peliculas y Series'
#os.chdir(path)
#dir = os.listdir(os.getcwd())
#for folder in dir:
#	if not (folder[0]=='P' or folder[0]=='S'):
#		os.rename(folder,'Pelicula - ' + folder)
		