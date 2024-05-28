#Importación del archivo que tiene la superclase para poder usar la herencia
from video import Video

#Clase Serie, que es una clase derivada de la clase Video
class Serie(Video):
    #Constructor
    def __init__(self, iden, titulo, director, clasificacion, anioEstreno, numTemporadas, numEpisodios):
        #En la línea de abajo se le indica los atributos que queremos que herede de la clase padre
        super().__init__(iden, titulo, director, clasificacion, anioEstreno)
        self.__numTemporadas = numTemporadas
        self.__numEpisodios = numEpisodios
        
    #Métodos getter's (Métodos de lectura)
    def getNumTemporadas(self):
        return self.__numTemporadas
    
    def getNumEpisodios(self):
        return self.__numEpisodios
