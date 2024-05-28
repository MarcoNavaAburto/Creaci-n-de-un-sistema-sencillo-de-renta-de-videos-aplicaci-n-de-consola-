#Importación del archivo que tiene la superclase para poder usar la herencia
from video import Video

#Clase Pelicula, que es una clase derivada de la clase video
class Pelicula(Video):
    #constructor
    def __init__(self, iden, titulo, director, clasificacion, anioEstreno, actorPrincipal, duracion):
        #En la línea de abajo se le indican los atributos que queremos que herede de la clase padre
        super().__init__(iden, titulo, director, clasificacion, anioEstreno)
        self.__actorPrincipal = actorPrincipal
        self.__duracion = duracion
        
    #Métodos getter's (métodos de lectura)
    def getActorPrincipal(self):
        return self.__actorPrincipal
    
    def getDuracion(self):
        return self.__duracion