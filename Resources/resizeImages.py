import os
from PIL import Image

# Set the path to the folder containing the images
folder_path = './images'

# Set the desired size of the images
desired_size = (500, 500)

# Iterate over all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Join the folder path and the filename to get the full path
        file_path = os.path.join(folder_path, filename)
        
        # Open the image using Pillow
        with Image.open(file_path) as im:
            # Resize the image to the desired size
            im_resized = im.resize(desired_size)
            
            # Save the resized image with the same filename
            im_resized.save(file_path)
