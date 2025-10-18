#!/usr/bin/env python3
"""
Super class: reusable by other clases.
Focus: Initialize flexible dictionaries and handle dictionary paths dynamically
"""

class CreateDictionary:
    """
    Clase reutilizable para inicializar diccionarios y preparar directorios.
    """
    def create_dictionary(self, **kwargs):
        """
        functions
        """
        return {**kwargs}
