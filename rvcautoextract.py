import os
import shutil
import zipfile

# Define the source folder containing the zip files
source_folder = 'F:/rvc/Retrieval-based-Voice-Conversion-WebUI/downloads'

# Define the destination folders
weights_folder = 'F:/rvc/Retrieval-based-Voice-Conversion-WebUI/assets/weights'
logs_folder = 'F:/rvc/Retrieval-based-Voice-Conversion-WebUI/logs'

# Function to extract and move files from zip archives
def extract_and_move(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('.pth'):
                zip_ref.extract(file, weights_folder)
            elif file.endswith('.index'):
                zip_ref.extract(file, logs_folder)

# Iterate through each zip file in the source folder
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith('.zip'):
            zip_file_path = os.path.join(root, file)
            extract_and_move(zip_file_path)

print("Extraction and moving completed successfully!")
