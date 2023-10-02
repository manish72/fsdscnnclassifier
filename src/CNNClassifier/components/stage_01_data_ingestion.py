import os
import urllib.request as request
from zipfile import ZipFile
from CNNClassifier import logger
from pathlib import Path
from tqdm import tqdm
from CNNClassifier.entity.config_entity import DataIngestionConfig
from CNNClassifier.utils import utils
from PIL import Image

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info("trying to download file")
            request.urlretrieve(
                url=self.config.Source_URL,
                filename=self.config.local_data_file
            )
            
        else:
            logger.info("file alreasdy exists")
    
    def get_updated_list_of_files(self,list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg")]
        
    
    def preprocess(self,zf,f,working_dir):
        target_filepath=os.path.join(working_dir,f)
        if not os.path.exists(target_filepath):
            zf.extract(f,working_dir)
    
    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file,mode="r") as zf:
            list_of_file=zf.namelist()
            updated_list_of_file=self.get_updated_list_of_files(list_of_file)
            for f in tqdm(updated_list_of_file):
                self.preprocess(zf, f, self.config.unzip_dir)

            # check for if any file in Cat and Dog folder is empty
            directory_contents = os.listdir(os.path.join(self.config.unzip_dir,"PetImages"))
            target_classes = list()
            
            for item in directory_contents:
                if os.path.isdir(os.path.join(self.config.unzip_dir,"PetImages",item)):
                    target_classes.append(item)
            
            logger.info("Checking if any image file is empty or corrupted")
            for class_name in target_classes:
                each_class_path = os.path.join(self.config.unzip_dir,"PetImages",class_name)
                image_list = os.listdir(each_class_path)
                for file in image_list:
                    file_path = os.path.join(each_class_path, file)
                    try:
                        img = Image.open(file_path) # open the image file
                        img.verify() # verify that it is, in fact an image
                    except (IOError) as e:
                        logger.error(f'Bad file: {file} exists in {each_class_path} folder, removing it.')
                        os.remove(file_path)
                        