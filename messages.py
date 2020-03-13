#-*-utf-8-*-
import datetime

#Declara una variable global
id_message = False

class Messages:
    '''
    Simula un mensaje enviado a un usuario como
    un serivicio de mensajeria
    '''
    def __init__(self, from_number="", text_of_sms="",has_been_viewed=""):
        """
        Inicializa un mensaje con el valores de from_number,
         time_arrived, text_of_sms enviadas por el usuario
         (separadas por coma). Automáticamentese inserta la vista
        """
        self.from_number = from_number
        self.text_of_sms = text_of_sms
        self.has_been_viewed = has_been_viewed
        self.create_time = datetime.date.today()
        global id_message
        id_message += 1
        self.id = id_message
    


    


