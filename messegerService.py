#-*- Coding: utf8-*-
#programa: messegerService.py
#objetivo Emula un servicio de mesajeria
#Autor: Diego Mauricio Diaz
#Fecha: 27/02/2020
import sys
import os
import platform


class ShortMessageService:
    '''
    Se encarga de la funcionalidad de enviar, resivir y
    ver los mensajes de una conversacion
    '''
    
    def __init__(self):
    '''incializa la bandeja de mensajes'''
    self.my_box = list
    self.options = {"1": self.add_new_arrival,
                        "2": self.message_count,
                        "3": self.get_unread_indexes,
                        "4": self.get_message,
                        "5": self.delete_message,
                        "6": self.clear}


