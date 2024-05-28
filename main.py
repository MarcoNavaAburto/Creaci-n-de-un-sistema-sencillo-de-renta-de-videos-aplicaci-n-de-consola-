#Importación del archivo para poder trabajar en el sistemad de videos
from sistemaVideo import SistemaVideo

#Clase Main, de todo el proyecto
class Main:
    
    #Variable para controlar el men� del sistema de videos
    otro = True
    
    #Creación de un objeto de tipo SistemaVideo
    sistemaVideo = SistemaVideo()
    
    #Ciclo que controla las operaciones que se pueden hacer en el men�
    while(otro):
        print("\nMenu de opciones del sistema de videos\n")
        print("Opcion\tAccion a realizar:\n1\t\tAgregar un video\n2\t\tEliminar un video")
        print("3\t\tRecibir la calificacion para un video\n4\t\tMostrar calificacion promedio de un video\n5\t\tMostrar numero de calificaciones recibidas de un video")
        print("6\t\tMostrar todo el catalogo de los videos disponibles\n7\t\tSalir")
        opcion = int(input("\nIngrese la opcion de la accion que desea realizar: "))
        
        match opcion:
            case 1:
                #Ejecución del método para agregar un video al catálogo
                sistemaVideo.agregarVideo()
                
            case 2:
                #Ejecución del método para eliminar un video del catálogo
                sistemaVideo.eliminarVideo()
    
            case 3:
                #Ejecución del método para recibir una calificación para un video
                sistemaVideo.recibirCalificacion()
                
            case 4:
                #Ejecución del método para mostrar la calificación promedio de un video
                sistemaVideo.mostrarCalificacionPromedioVideo()
            
            case 5:
                #Ejecución del método para revisar el número de calificaciones que ha recibido un video
                sistemaVideo.mostrarNumeroCalificacionesVideo()
            
            case 6:
                #Ejecución del método para mostrar los videos que hay en el catálogo
                sistemaVideo.mostrarCatalogo()
            
            case 7:
                otro = False
            case _:
                print("\nLa opcion ingresada es incorrecta\n")
                
    
    #Mensaje de despedida
    print("\nFin de la ejecucion del programa\n")            
        
