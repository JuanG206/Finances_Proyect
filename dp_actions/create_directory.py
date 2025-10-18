#!/usr/bin/env python3
"""
Super class: reusable by other clases.
Focus: Initialize flexible dictionaries and handle dictionary paths dynamically
"""
import os

class CreateDirectory:
    """
    Resuable class that create a new directory if it doesnt exist and
    return the complete path.
    """

    def __init__(self, directory):
        self.base_path = os.getcwd()

        if directory:
            self.directory = os.path.join(self.base_path, directory)
            os.makedirs(self.directory, exist_ok=True)
        else:
            self.directory = self.base_path
