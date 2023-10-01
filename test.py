from pathlib import Path

print(Path("x/y/z.txt"))

# check if there is any corrupted file inside PetImages folder, execute below code
'''from os import listdir
from PIL import Image

image_list = listdir('D:/ineuron/Projects/DL/fsdscnnclassifier/artifacts/data_ingestion/PetImages/Dog')

for filename in image_list:
    if filename.endswith('.jpg'):
        try:
            img = Image.open("D:/ineuron/Projects/DL/fsdscnnclassifier/artifacts/data_ingestion/PetImages/Dog/"+filename) # open the image file
            img.verify() # verify that it is, in fact an image
        except (IOError) as e:
            print('Bad file:', filename)'''