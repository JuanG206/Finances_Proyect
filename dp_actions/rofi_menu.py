#!/usr/bin/env python3
"""
Clase para mostrar menús con Rofi
"""

import subprocess

class Rofimenu:
    """
    Clase que usa Rofi para mostrar menús interactivos desde Python.
    """

    def rofi_menu(self, options, prompt="Select an option:"):
        """
        Muestra un menú usando Rofi y devuelve la opción seleccionada.
        """
        try:
            options_str = "\n".join(options)
            result = subprocess.run(
                ["rofi", "-dmenu", "-p", prompt],
                input=options_str.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False
            )
            return result.stdout.decode().strip()
        except FileNotFoundError:
            print("Rofi no está instalado o no se encuentra en el PATH.")
            return None

