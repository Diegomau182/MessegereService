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

    def add_new_arrival(self, from_number="", text_of_sms=""):
        """ Crea un nuevo mensaje y la agrega a la bandeja """
        self.my_box.append(Messages(from_number, text_of_sms)) 

    def message_count(self):
        """Retorna la cantidad total de mensajes sms en la bandeja"""
        en_Lista = str(len(self.my_box))

    def get_unread_indexes(self):
        """Retorna una lista con los índices de todos los SMS sin leer."""
        for msm in self.:
            if str(m.id) == str(note_id):
                return note