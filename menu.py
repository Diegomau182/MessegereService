# -*- coding: utf8 -*-
import sys
import os
import platform
from service_message import ShortMessageService


class Menu:
    """
    Despliega un menú que responde a las elecciones del usuario.
    """

    def __init__(self):
        self.service_message = ShortMessageService()
        self.options = {"1": self.add_new_arrival,
                        "2": self.message_count,
                        "3": self.get_unread_indexes,
                        "4": self.get_message,
                        #"5": self.delete_message,
                        #"6": self.clear,
                        "7":self.exit
                        }

    def display_menu(self):
        """ Despliega el menú principal """
        self.clear_screen()
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

    def press_enter(self):
        """ Realiza una pausa y solicita presionar una tecla """
        input("\nPresiona Enter para continuar")

    def clear_screen(self):
        """
        Verifica mediante la librería platform el sistema operativo
        del usuario y limpia la pantalla dependiendo del SO utilizado.
        """
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")
        else:
            print("Plataforma no soportada")


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
        self.clear_screen()
        from_number = input("Ingrese el numero: ")
        text_of_sms = input("Agrege el mensaje: ")
        has_been_view="noleido" 
        self.service_message.add_new_arrival(from_number, text_of_sms, has_been_view)
        print("¡Nuevo Mensaje agregado!")
        self.press_enter()
    
    def message_count(self):
        self.service_message.message_count()
        self.press_enter()

    def get_unread_indexes(self, leido="noleido"):
        self.clear_screen
        """ Busca un Mensaje no leido """
        My_box = self.service_message.my_box
        for box in My_box:
            if str(box.has_been_viewed) == str(leido):
                print("Id: {0}\nNumero: '{1}'\ntexto: {2}\nFecha: {3} {4}"
                .format(box.id, box.from_number, box.text_of_sms, box.create_time, box.has_been_viewed))
           
        self.press_enter()

    def get_message(self):
        """ Despliega una nota """
        leido="leido"
        idmensage = input("Ingrese el id del mensaje: ")
        My_box = self.service_message.my_box
        for box in My_box:
            if str(box.id) == str(idmensage):
                print("Id: {0}\nNumero: '{1}'\ntexto: {2}\nFecha: {3} {4}"
                .format(box.id, box.from_number, box.text_of_sms, box.create_time, box.has_been_viewed))
                self.service_message.modify_message(box.id, box.from_number,box.text_of_sms,leido)
        self.press_enter()

    def exit(self):
        """ Cierra el reproductor musical. """
        print("Gracias por utilizar nuestro Servicios de Mensajeria.")
        sys.exit()
        
if __name__ == "__main__":
    menu = Menu()
    menu.run()