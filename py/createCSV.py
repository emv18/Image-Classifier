import csv
import os

def create_csv(data_list, filename):
    #print(data_list)
    folder_path = "Data"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Value'])
        writer.writerows([[value] for value in data_list])
