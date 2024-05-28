#Clase Video, que es la superclase
class Video:
    #Constructor
    def __init__(self, iden, titulo, director, clasificacion, anioEstreno):
        self.__id = iden
        self.__titulo = titulo
        self.__director = director
        self.__clasificacion = clasificacion
        self.__anioEstreno = anioEstreno
        self.__califRecibidas = 0
        self.__calPromedio = 0
        self.__sumaCalificaciones = 0
        
        
    #Métodos getter's (métodos de lectura)
    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo
    
    def getDirector(self):
        return self.__director
    
    def getClasificacion(self):
        return self.__clasificacion
    
    def getAnioEstreno(self):
        return self.__anioEstreno
    
    def getCalifRecibidas(self):
        return self.__califRecibidas
    
    #Método para calcular el promedio de calificaciones de un video
    def getCalPromedio(self):
        if self.__califRecibidas != 0:
            self.__calPromedio = self.__sumaCalificaciones / self.__califRecibidas
            
        return self.__calPromedio
    
    #Método para que ira sumando las calificaciones que vaya recibiendo el video, e irá sumando el número de calificaciones que han sido recibidas para un video
    def asignarCalificacionVideo(self, calificacion):
        self.__sumaCalificaciones = self.__sumaCalificaciones + calificacion
        self.__califRecibidas = self.__califRecibidas + 1