#!/usr/bin/env python3
"""Module: SaveToJson - handles saving data into JSON files"""

import os
import json
from datetime import datetime
from dp_actions.create_directory import CreateDirectory


class Save:
    """
    Class that extract data from a called class, insert into a json File
    and CreateDirectory class is call to create a new directory where
    the json file is stored
    """
    def __init__(self, directory):
        self.directory = CreateDirectory(directory).directory

    def savetojson(self, data, data_name):
        """
        Save the recieved dictionary in a json file inside the directory
        """

        day_time = datetime.now().strftime("Date:%d-%m-%y,hour:%H:%M")
        filename = f"{data_name}_{day_time}.json"
        filepath = os.path.join(self.directory, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        msg = f"""\nFile succesfully saved at :\n{os.path.abspath(filepath)}"""
        print(msg)
        return filepath
