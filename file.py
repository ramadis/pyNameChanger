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
print '-c Carpetas' #p1
print '-a Archivos' #p1 // todos #p2
print 'nom-- Que comience con nom'
print '--nom Que termine con nom'
print '--nom-- Que contenga nom'
print '! Negador' #p3
print ''
parametro = str(raw_input("Parametro: "))

p1=False
p2=False

if '-c' in parametro:
	p1=True
elif '-a' in parametro:
	p1=False
elif '*' in parametro:
	p2=True

dir = [x for x in os.listdir(path) if (os.path.isdir(x) and p1) or p2]
print dir

#Elector de cambios
print 'Cambios y condiciones:'
print ''
print '*nnom Agregar al final'
print 'nnom* Agregar al principio'
print ''
comando = str(raw_input("Comando: "))

for folder in dir:
	if comando[0]='*':
		os.rename(folder,folder + comando[1:])
	elif comando[len(comando)-1]:
		os.rename(folder,folder + comando[:len(comando)-1])
	else:
		os.rename(folder,comando)

	
#path = r'C:\Users\Ramiro\Desktop\Peliculas y Series'
#os.chdir(path)
#dir = os.listdir(os.getcwd())
#for folder in dir:
#	if not (folder[0]=='P' or folder[0]=='S'):
#		os.rename(folder,'Pelicula - ' + folder)
		