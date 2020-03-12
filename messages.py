#-*-utf-8-*-
import datetime


class Messages:
    '''
    Simula un mensaje enviado a un usuario como
    un serivicio de mensajeria
    '''
    def __init__(self, from_number="", text_of_sms=""):
        """
        Inicializa un mensaje con el valores de from_number,
         time_arrived, text_of_sms enviadas por el usuario
         (separadas por coma). Automáticamentese inserta la vista
        """
        self.from_number = from_number
        self.text_of_sms = text_of_sms
        self.create_time = datetime.date.today()
        self.visto = 0

    


