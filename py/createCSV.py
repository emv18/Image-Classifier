import csv
import os

# This piece of code was to create a csv with one feature

def create_csv(data_list, filename):
    #print(data_list)
    #folder_path = "Data/Samoyed"
    folder_path = "Data/Pomeranian"
    #folder_path = "Data/Xolitzquintle"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['value'])
        writer.writerows([[value] for value in data_list])
'''

def create_csv(colors, filename):
    #folder_path = "Data/Samoyed"
    #folder_path = "Data/Pomeranian"
    folder_path = "Data/Xolitzquintle"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["color", "value"])  # Write column names
        
        for color, values in colors.items():
            for value in values:
                writer.writerow([color, value])
            '''
