#!/usr/bin/env python3
import os
import platform

class Cleanterminal:
    """
    Class that works a terminal cleaning
    """

    def cleaning_terminal(self):
        """
        Cleans the terminal in windows,linux
        """
        print("Cleaning terminal!")
        comando = 'cls' if platform.system() == "Windows" else "clear"
        os.system(comando)
