import os
import csv
from read_erg_files import ReadERGFiles

def extract_parameter_names(file_path):
    parameter_names = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('File.At.') and '.Name =' in line:
                parameter_name = line.split('=')[1].strip()
                parameter_names.append(parameter_name)
    return parameter_names

# Specify the directory containing the files
directory_path = os.path.join(os.getcwd(), "read_erg_files\\erg_files")
print(directory_path)

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.erg.info'):
        file_path = os.path.join(directory_path, filename)
        parameters = extract_parameter_names(file_path)
        
        # Initialize the ERG file object
        erg_file_path = file_path.replace('.info', '')
        ERGFileObj = ReadERGFiles(erg_file_path)
        
        # Ensure 'Time' is the first parameter and exists
        if 'Time' not in parameters:
            print(f"Warning: 'Time' parameter not found in {filename}")
            continue
        else:
            parameters.remove('Time')
            parameters.insert(0, 'Time')
        
        # Fetch values for each parameter
        all_values = {}
        max_length = 0
        for param in parameters:
            values = ERGFileObj.get_value_for_parameters(param)
            if values is not None and 'value' in values:
                all_values[param] = values['value']
                if len(values['value']) > max_length:
                    max_length = len(values['value'])
            else:
                print(f"Warning: No values found for parameter {param}")
                all_values[param] = [None] * max_length  # Ensure all parameters have the same length

        # Ensure all lists have the same length by padding with None
        for param in all_values:
            if len(all_values[param]) < max_length:
                all_values[param].extend([None] * (max_length - len(all_values[param])))
        
        # Define the CSV file name
        csv_filename = f"{filename.replace('.erg.info', '')}_values.csv"
        csv_file_path = os.path.join(directory_path, csv_filename)
        
        # Save values to a CSV file
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(parameters)  # Write header
            
            # Write values row by row
            for i in range(max_length):
                row = [all_values[param][i] for param in parameters]
                csv_writer.writerow(row)
        
        print(f'Saved values to {csv_filename}')
