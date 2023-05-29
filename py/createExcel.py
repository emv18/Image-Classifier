import os
import pandas as pd
from PIL import Image

# Set the path to the folder containing the images
folder_path = './Images/All Dogs/'

# Initialize empty lists to store the image names, ids, and types
image_names = []
image_ids = []
image_types = []

# Iterate over all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Append the filename to the list of image names
        image_names.append(filename)
        
        # Get the id of the image and append it to the list of image ids
        image_id = os.path.splitext(filename)[0]
        image_ids.append(image_id)
        
        # Determine the type of the image based on its id and append it to the list of image types
        image_number = int(image_id.split('perro')[1])
        if image_number <= 218:
            image_type = 'samoyedo'
        elif image_number <= 437:
            image_type = 'pomerania'
        else:
            image_type = 'xolo'
        image_types.append(image_type)

# Create a Pandas DataFrame from the lists of image names, ids, and types
df = pd.DataFrame({'Image Name': image_names, 'Image ID': image_ids, 'Image Type': image_types})

# Create an Excel file from the DataFrame
df.to_excel('image_names_ids_and_types.xlsx', index=False)

