#Importación del archivo que tiene la superclase para poder usar la herencia
from video import Video

#Clase Documental, que es una clase derivada de la clase Video
class Documental(Video):
    #Constructor
    def __init__(self, iden, titulo, director, clasificacion, anioEstreno, tema, productor):
        #En la línea de abajo le indicamos los atributos que queremos heredar de la clase padre
        super().__init__(iden, titulo, director, clasificacion, anioEstreno)
        self.__tema = tema
        self.__productor = productor
        
    #Métodos getter's (métodos de lectura)
    def getTema(self):
        return self.__tema
    
    def getProductor(self):
        return self.__productor

