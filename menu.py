# -*- coding: utf8 -*-
import sys
import platform
from service_message import ShortMessageService


class Menu:
    """
    Despliega un menú que responde a las elecciones del usuario.
    """

    def __init__(self):
        self.service_message = ShortMessageService()
        self.options = {"1": self.add_new_arrival,
                        #"2": self.message_count,
                        #"3": self.get_unread_indexes,
                        #"4": self.get_message,
                        #"5": self.delete_message,
                        #"6": self.clear,
                        #"7":self.exit
                        }

    def display_menu(self):
        """ Despliega el menú principal """
        print("""
             Menú principal
             1. Agrega un nuevo Mensaje
             2. Cuenta los mensajes
             3. Muestra los mensajes no leidos
             4. Busca un mensaje
             5. Borra un mensaje
             6. Borra todos los mensajes
             7. Salir
             """)

    def run(self):
        """ Método de entrada para la aplicación """
        while True:
            self.display_menu()
            choise = input("Ingrese una opción: ")
            action = self.options.get(choise)

            if action:
                action()
            else:
                print("¡{0} no es una opción válida!".format(choise))
    
    def add_new_arrival(self):
        from_number = input("Ingrese el numero: ")
        text_of_sms = input("Agrege el mensaje: ")
        has_been_view="noleido" 
        self.service_message.add_new_arrival(from_number, text_of_sms, has_been_view)
        print("¡Nuevo Mensaje agregado!")
    


if __name__ == "__main__":
    menu = Menu()
    menu.run()