#  Copyright (c) 2020:      IPG Automotive GmbH
#  Bannwaldallee 60         Phone  +49.721.98520.0
#  76185 Karlsruhe          Fax    +49.721.98520.99
#  Germany                  www    www.ipg-automotive.com
#  last author: ksh
import os
import struct
from typing import Union
from cm_infofiles import InfoFile


class ReadERGFiles:
    """
    :param erg_file_path: absolute path of the erg file o be read.

    Class to read binary .erg [ERG-2 only] and return stored data in the correct datatype as
    mentioned in the .erg.info file.

    To run it, instantiate the class using the erg file path as the argument
    eg: ReadERG_Obj = ReadERGFiles("C:\CM\TestRun.erg")

    Make sure to save the accompanying .erg.info file ('TestRun.erg.info') in the same folder as the
     .erg file

    When the object is in instantiated, the following class variables are available: -
    ReadERGObj.no_of_parameters: Gives the number of parameters in the .erg.info file -
    ReadERGObj.path: Gives the path of the erg file which was given as the argument -
    ReadERGObj.erg_info_file: Gives the path of the info-file accompanying the erg file -
    ReadERGObj.self.parameters_with_values: Gives the complete list of all parameters with each
        parameter entry in the form of a dictionary with all the information in the erg file - This
        dictionary contains the name of the parameter, data-type, unit and the values.

    The two methods that can be accessed are:
    ReadERGObj.get_dict_of_parameters(): Returns all the parameters in the erg file along with units
    ReadERGObj.get_value_for_parameters('parameter_name'): Returns a dictionary with parameter name,
        parameter unit and the values

    """

    def __init__(self, erg_file_path):
        self.path = erg_file_path  # location of the erg file
        self.erg_info_file = self.path + ".info"  # location of the erg.info file
        self._parameters_list = self._read_parameters_from_info_file()  # read info file
        self.parameters_with_values = self._get_values_in_erg_file()  # complete list of all
        # parameters with each parameter entry in the form of a dictionary with all the
        # information in the erg file - This dictionary contains the name of the parameter,
        # data-type, unit and the values.

    def _read_parameters_from_info_file(self):
        """
        Returns dictionary with all parameters
        """
        i = 0
        if not os.path.isfile(self.path):
            raise FileNotFoundError("ERG file doest exist.")
        if not os.path.isfile(self.erg_info_file):
            raise FileNotFoundError("ERG info file does not exist. Please copy it in the same "
                                    "folder as the erg file!")
        info = InfoFile(self.erg_info_file)
        parameters_list = []
        self.no_of_parameters = 0

        while 1:
            i = i + 1
            if info.get_string(f"File.At.{i}.Name") == '':
                i = i - 1
                break
            unit_key = "Quantity." + info.get_string(f"File.At.{i}.Name") + ".Unit"
            dict_quant = {"name" : info.get_string(f"File.At.{i}.Name"),
                          "type" : info.get_string(f"File.At.{i}.Type"),
                          "unit" : info.get_string(unit_key),
                          "value": []}
            parameters_list.append(dict_quant)
            self.no_of_parameters = i
        for line in parameters_list:
            if "$none$" == line["name"]:
                parameters_list.remove(line)
                self.no_of_parameters = i - 1

        return parameters_list

    def _get_values_in_erg_file(self):
        """
        get sim data for particular quantity
        """
        with open(self.path, "rb") as binary_file:
            value = binary_file.read()
            len_byte = len(value)
            n = 1
            i = 16
            while i < len_byte:
                # loop each Record
                for k in range(len(self._parameters_list)):
                    if self._parameters_list[k]['type'] == 'Double':
                        byte_size = 8
                        byte_code = 'd'
                    elif self._parameters_list[k]['type'] == 'Float':
                        byte_size = 4
                        byte_code = 'f'
                    elif self._parameters_list[k]['type'] == 'Int':
                        byte_size = 4
                        byte_code = 'i'
                    binary_file.seek(i)
                    val = binary_file.read(byte_size)
                    final_value = struct.unpack(byte_code, val)
                    self._parameters_list[k]["value"].append(final_value[0])
                    i = i + byte_size
                while i % 8 > 0:
                    i = i + 1
                n = n + 1
        return self._parameters_list

    def get_dict_of_parameters(self):
        """
        returns list of parameters with units
        """
        output = []
        output_dict = {}
        for line in self._parameters_list:
            output_dict.update({line["name"]: line["unit"]})
            output.append({line["name"]: line["unit"]})
        return output_dict

    def get_value_for_parameters(self, parameter: Union[list, str]):
        """
        Returns values for a list of parameters
        :param parameter:
        """
        output = None
        if type(parameter) == list:
            output = []
            for ele in parameter:
                for line in self.parameters_with_values:
                    if ele == line["name"]:
                        output.append(
                            {"name": line["name"], "unit": line["unit"], "value": line["value"]})
        else:
            for line in self.parameters_with_values:
                if parameter == line["name"]:
                    output = {"name": line["name"], "unit": line["unit"], "value": line["value"]}

        return output
