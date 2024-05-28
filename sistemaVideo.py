#Importación del archivo que contiene la implementación de la clase Video
from video import Video
#Importación del archivo que contiene la implementación de la clase Pelicula
from pelicula import Pelicula
#Importación del archivo que contiene la implementación de la clase Serie
from serie import Serie
#Importación del archivo que contiene la implementación de la clase Documental
from documental import Documental

#Clase SistemaVideo
class SistemaVideo:
    #Constructor
    def __init__(self):
        self.__catalogo = [] #Se crea lista vací que es donde se irán guardando la información de los videos

    #Método que sirve para identificar el tipo de video que se añadira al catálogo
    def agregarVideo(self):
        
        iden = False
        
        try:
        
            while iden == False:
                identificador = int(input("\nIngrese un identificador: "))
                iden = self.__validarIdentificador(identificador)
                if iden == False:
                    print("\nFavor de ingresar un identificador diferente ya que no pueden haber repeticiones")
                else:
                    print("\nEl identificador que se registro es correcto")
        
        
            #Se define que tipo de video se va a guardar en el catalogo y se manda el objeto para terminar de crear el objeto por completo
            tipo = int(input("\nOpcion\tTipo de video\n1\t\tPelicula\n2\t\tSerie\n3\t\tDocumental\nIngrese el tipo de video que registrara en el sistema: "))
        
            while tipo < 1 or tipo > 3:
                print("\Favor de ingresar una de las opciones validas")
            
            if tipo == 1:
                self.__agregarPelicula(identificador)
            
            if tipo == 2:
                self.__agregarSerie(identificador)
            
            if tipo == 3:
                self.__agregarDocumental(identificador)
        
        except ValueError:
            print("\nSe ingreso un tipo de dato incorrecto")
            
            
    #Método para validar un identificador (se requiere no repetir identificadores ya que no puede haber repeticiones)        
    def __validarIdentificador(self, identificador):
        #Ciclo for que recorre la lista del catálogo para ver si hay un identificador repetido
        if len(self.__catalogo) == 0:
            return True
        
        else:    
            for obj in self.__catalogo:
                if identificador == obj.getId():
                    return False
                    break
        
    #Método que sirve para agregar una PELICULA al catalogo de videos
    def __agregarPelicula(self, identificador):
        #Proceso para agregar una pelicula al catalogo
        titulo = input("\nIngrese el titulo de la pelicula: ")
        director = input("Ingrese el nombre del director de la pelicula: ")
        clasificacion = input("Ingrese el tipo de clasificacion de la pelicula: ")
        anioEstreno = input("Ingrese la fecha del anio de estreno de la pelicula: ")
        actorPrincipal = input("Ingrese el nombre del actor principal de la pelicula: ")
        duracion = input("Ingrese el tiempo de duracion de la pelicula en minutos: "
                         )
        #Creación de un objeto de tipo Pelicula
        pelicula = Pelicula(identificador, titulo, director, clasificacion, anioEstreno, actorPrincipal, duracion)
        
        #Se agrega la película al catálogo
        self.__catalogo.append(pelicula)
        
        #Mensaje de que se agregó correctamente al catálogo de videos
        print("\nEl video se ha agregado correctamente al catalogo de videos")
            
        
    #Método que sirve para agregar una SERIE al catalogo
    def __agregarSerie(self, identificador):
        #Proceso para agregar una serie al catalogo
        
        try:
            titulo = input("\nIngrese el titulo de la serie: ")
            director = input("Ingrese el nombre del director de la serie: ")
            clasificacion = input("Ingrese el tipo de clasificacion de la serie: ")
            anioEstreno = input("Ingrese la fecha del anio de estreno de la serie: ")
            numTemporadas = int(input("Ingrese el numero de de temporadas de la serie: "))
            numEpisodios = int(input("Ingrese el numero de episodios de la serie: "))
        
            #Creación de un objeto de tipo serie
            serie = Serie(identificador, titulo, director, clasificacion, anioEstreno, numTemporadas, numEpisodios)
    
            #Se agregar la serie al catalogo
            self.__catalogo.append(serie)
        
            #Mensaje de que se agregó la serie correctamente al catálogo de videos
            print("\nLa serie se ha agregado correctamente al catalogo de videos")
        
        except ValueError:
            print("\nSe ingreso un tipo de dato incorrecto")
        
    #Método que sirve para agregar un documental al catalogo
    def __agregarDocumental(self, identificador):
        titulo = input("\nIngrese el titulo del documental: ")
        director = input("Ingrese el nombre del director del documental: ")
        clasificacion = input("Ingrese el tipo de clasificacion del documental: ")
        anioEstreno = input("Ingrese la fecha del anio de estreno del documental: ")
        tema = input("Ingrese el tipo de tema del documental: ")
        productor = input("Ingrese el nombre del productor del documental: ")
        
        #Creación de un objeto de tipo Documental
        documental = Documental(identificador, titulo, director, clasificacion, anioEstreno, tema, productor)
        
        #Se agrega el documental al catalogo
        self.__catalogo.append(documental)
        
        #Mensaje de que se agregó correctamente el documental al catálogo de videos
        print("\nEl documental se ha agregado correctamente al catalogo de videos")
       
    #Método que sirve para eliminar un video del catálogo
    def eliminarVideo(self):
        #Se solicita el identificador al usuario
        try:
            identificador = int(input("\nIngrese el identificador del video que desea borrar del catalogo de videos: "))
            encontrado = False
        
            #Se busca en la lista del catalogo el ID que se ingresó para eliminar el video
            for obj in self.__catalogo:
                if obj.getId() == identificador:
                    encontrado = True
                    self.__catalogo.remove(obj)
                    break
            
            if encontrado:
                print("\nEl video ha sido borrado del catalogo")
            else:
                print("\nEl video no se encuentra en la lista")
        
        except ValueError:
            print("\nNo se ingreso un tipo de dato correcto")
    
    #Método que sirve para asignar una calificación a un video
    def recibirCalificacion(self):
        #Se inicializa una variable con valor de False, en dado de que el video que se quiere calificar no se cambiará su valor
        encontrado = False
        
        try:
            #Se ingresa el ID del video que se desea calificar
            idBuscar = int(input("\nIngrese el id del video que desea calificar: "))
        
            #Se hace la búsqueda del ID que se desea buscar
            for video in self.__catalogo:
                if video.getId() == idBuscar:
                    self.__asignarCalificacion(video)
                    encontrado = True
                    break
            
            #Se le indica al usuario si el video fue encontrado o no
            if encontrado:
                print("\nEl video ha sido calificado de manera exitoso")
            else:
                print(f"\nEl video con id {idBuscar} no se encuentra en el catalogo")
        
        except ValueError:
            print("\nSe ingreso un tipo de dato incorrecto")
            
    
    #Método para asginar calificación a un video que si se encuentra en el catálogo
    def __asignarCalificacion(self, video):
         
        try:
            #Obteniendo la calificacion que se le quiere dar al video
            calificacion = float(input("\nIngrese la calificacion que le quiere dar al video: "))
        
            #Se ejecuta el método para asignar la calificación al video
            video.asignarCalificacionVideo(calificacion)
        except ValueError:
            print("\nSe ingreso un tipo de dato incorrecto")
        
    
    #M+etodo que sirve para mostrar el promedio de calificaciones de un video
    def mostrarCalificacionPromedioVideo(self):
        encontrado = False
        
        try:
            idBuscar = int(input("\nIngrese el ID del video que desea saber la calificacion promedio: "))
        
            for video in self.__catalogo:
                if video.getId() == idBuscar:
                    video.getCalPromedio()
                    print(f"\nID del video: {video.getId()}\nTitulo del video: {video.getTitulo()}\nPromedio de calificaciones: {video.getCalPromedio():.2f}")
                    encontrado = True
                
            if encontrado == False:
                print("\nEl video no se encuentra en el catalogo")
                
        except ValueError:
            print("\nSe ingreso un tipo de dato incorrecto")
    
    #Método que sirve para mostrar el número de calificaciones que ha recibido un video
    def mostrarNumeroCalificacionesVideo(self):
        encontrado = False
        
        try:
            #Se solicita el ID del video
            idBuscar = int(input("\nIngrese el ID del video que desear ver el numero de calificaciones recibidas: "))
        
            #Se hace la búsqueda del ID que se ingreso
            for video in self.__catalogo:
                if video.getId() == idBuscar:
                    self.__mostrarCalificacionesRecibidas(video)
                    encontrado = True
                    break
            
            #Se le indica al usuario si el ID fue encontrado o no
            if encontrado == False:
                print(f"\nEl video con Id {idBuscar} no se encuentra en el catalogo\n")
        
        except ValueError:
            print("\nSe ingreso un tipo de dato incorrecto")
                
    #Método que muestra las calificaciones recibidas para un video, como el Id y el título correspondiente
    def __mostrarCalificacionesRecibidas(self, video):
        print("\nInformacion del video\n")
        print(f"ID del video: {video.getId()}\nNombre del video: {video.getTitulo()}\nCalificaciones recibidas: {video.getCalifRecibidas()}\n")
        
    
    #Método que selecciona el tipo de video que va a mostrar en pantalla, identifica que tipo de objeto y lo manda a un método donde imprime la información correspondiente
    def mostrarCatalogo(self):
        
        #Proceso para mostrar la información del catalogo
        if len(self.__catalogo) == 0:
            print("\nNo hay videos en el catalogo")
        else:
            
            for video in self.__catalogo:  
                video.getCalPromedio()
                if isinstance(video, Pelicula):
                    self.__mostrarInformacionPelicula(video)
            
                elif isinstance(video, Serie):
                    self.__mostrarInformacionSerie(video)
            
                else:
                    self.__mostrarInformacionDocumental(video)
          
    #Muestra la información correspondiente a una película
    def __mostrarInformacionPelicula(self, video):
        
        print("*" * 80)
        print(f"Id de la pelicula: {video.getId()}")
        print(f"Titulo de la pelicula: {video.getTitulo()}")
        print(f"Director de la pelicula: {video.getDirector()}")
        print(f"Clasificacion de la pelicula: {video.getClasificacion()}")
        print(f"Anio de estreno de la pelicula: {video.getAnioEstreno()}")
        print(f"Cantidad de calificaciones recibidas: {video.getCalifRecibidas()}")
        print(f"Promedio de calificaciones: {video.getCalPromedio():.2f}")
        print(f"Actor principal: {video.getActorPrincipal()}")
        print(f"Duracion de la pelicula en minutos: {video.getDuracion() }")
    
    #Muestra la información correspondiente a una serie
    def __mostrarInformacionSerie(self, video):
        print("*" * 80)
        print(f"Id de la serie: {video.getId()}")
        print(f"Titulo de la serie: {video.getTitulo()}")
        print(f"Director de la serie: {video.getDirector()}")
        print(f"Clasificacion de la serie: {video.getClasificacion()}")
        print(f"Anio de estreno de la serie: {video.getAnioEstreno()}")
        print(f"Cantidad de calificaciones recibidas: {video.getCalifRecibidas()}")
        print(f"Promedio de calificaciones: {video.getCalPromedio():.2f}")
        print(f"Numero de temporadas: {video.getNumTemporadas()}")
        print(f"Numero de episodios de toda la serie: {video.getNumEpisodios()}")
        
    #Muestra la información correspondiente a un documental
    def __mostrarInformacionDocumental(self, video):
        print("*" * 80)
        print(f"Id del documental: {video.getId()}")
        print(f"Titulo del documental: {video.getTitulo()}")
        print(f"Director del documental: {video.getDirector()}")
        print(f"Clasificacion del documental: {video.getClasificacion()}")
        print(f"Anio de estreno del documental: {video.getAnioEstreno()}")
        print(f"Cantidad de calificaciones recibidas: {video.getCalifRecibidas()}")
        print(f"Promedio de calificaciones: {video.getCalPromedio():.2f}")
        print(f"Nombre del tema del documental: {video.getTema()}")
        print(f"Nombre del tema del productor: {video.getProductor()}")
