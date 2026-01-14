#!/usr/bin/env python3
"""
Module: file_manager
Handles saving, loading, and deleting data in TXT files.
"""

import os


class FileManager:
    """
    File manager to persist objects as TXT files.
    """

    def __init__(self, folder_path):
        """Initialize the folder path and create it if it doesn't exist."""
        self.folder_path = folder_path
        os.makedirs(folder_path, exist_ok=True)

    def save(self, obj_id: str, data: dict):
        """
        Save a dictionary to a TXT file named after the obj_id.
        Each line: key=value
        """
        path = os.path.join(self.folder_path, f"{obj_id}.txt")
        with open(path, "w", encoding="utf-8") as f:
            for key, value in data.items():
                f.write(f"{key}={value}\n")

    def load(self, obj_id: str):
        """
        Load a dictionary from a TXT file by obj_id.
        """
        path = os.path.join(self.folder_path, f"{obj_id}.txt")
        if not os.path.exists(path):
            return None
        data = {}
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                key, value = line.strip().split("=", 1)
                data[key] = value
        return data

    def load_all(self):
        """
        Load all TXT objects in the folder as dictionaries.
        """
        items = []
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                with open(os.path.join(self.folder_path, filename), "r",
                          encoding="utf-8") as f:
                    data = {}
                    for line in f:
                        key, value = line.strip().split("=", 1)
                        data[key] = value
                    items.append(data)
        return items

    def delete(self, obj_id: str):
        """Delete a TXT file by obj_id."""
        path = os.path.join(self.folder_path, f"{obj_id}.txt")
        if os.path.exists(path):
            os.remove(path)
