#Imports
import os #Importa el simbolo de sistema

#Inicializo variables
dir = [] #Almacena los archivos y carpetas
path = r'' #Almacena la direccion

################
####Programa####
################

dir = os.listdir(os.getcwd())

print 'Estas en ' + os.getcwd()
print ''
for x in 

path = r'C:\Users\Ramiro\Desktop\Peliculas y Series'

os.chdir(path)

dir = os.listdir(os.getcwd())

for folder in dir:
	if not (folder[0]=='P' or folder[0]=='S'):
		os.rename(folder,'Pelicula - ' + folder)
		