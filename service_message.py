#-*-utf-8-*-
from messages import Messages

class ShortMessageService:
    """
    Representa una colección de Mensajeria que pueden ser
    agregada, buscada y eliminada.
    """

    def __init__(self):
        """ Inicializa una bandeja Vacia """
        self.my_box = list()

    def add_new_arrival(self, from_number="", text_of_sms="",has_been_viewed=""):
        """ Crea un nuevo mensaje y la agrega a la bandeja """
        self.my_box.append(Messages(from_number, text_of_sms, has_been_viewed)) 

    def message_count(self):
        """Retorna la cantidad total de mensajes sms en la bandeja"""
        print("Se encontraron en bandeja ",len(self.my_box)," Mensajes")

    def get_unread_indexes(self, has_been_viewed ="noleido"):
        """Retorna una lista con los índices de todos los SMS sin leer."""
        for msm in self.my_box:
            if str(msm.has_been_viewed) == str(has_been_viewed):
                return msm
    

    def _search_note(self, id_message):
        """
        Busca un mensaje con el id enviado.
        Esta función es privada 
        """
        for msm in self.my_box:
            if str(msm.id) == str(id_message):
                
                return msm
        
        return None
    
    def delete_message(self, id_message):
        """Elimina uno de los mensajes en la bandeja"""
        msm = self._search_note(id_message)

        if msm:
            self.my_box.remove(id_message)
            return True
        else:
            print("No existe una nota con el id: {0}"
            .format(id_message))
            return False
    
    def clear(self):
        """Elimina todos los mensaje de la bandeja"""
        for msm in self.my_box:
            msm.remove(id)



