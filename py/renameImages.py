import os

# Set the path to the folder containing the images
folder_path = './xolo'

# Initialize a counter for the consecutive numbers
counter = 438

# Iterate over all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Create the new filename by concatenating "perro" and the counter
        new_filename = f"perro{counter}.jpg"
        
        # Join the folder path and the old filename to get the full old path
        old_path = os.path.join(folder_path, filename)
        
        # Join the folder path and the new filename to get the full new path
        new_path = os.path.join(folder_path, new_filename)
        
        # Rename the file using the new path
        os.rename(old_path, new_path)
        
        # Increment the counter
        counter += 1