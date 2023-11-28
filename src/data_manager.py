import os
from pathlib import Path
import pymongo

class Data_Manager:
    def __init__(self, project_name):
        self.project_name = project_name
        
        self.create_mongo_connection()
        self.operate_mongo_db()
        
        
    # Making operation on mongo db to retrieve information
    
    def operate_mongo_db(self):
        self.create_record()
    
    # Creating database with MongoDB
    def create_mongo_connection(self):
        
        try:
            client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
            self.mydb = client['ALL_Data_Database']
            self.collections = self.mydb['project_database']
        
        except Exception as e:
            print(e)
    
    def get_image_label_list(self):
        self.image_folder_path = Path(f"uploads/{self.project_name}/images")
        self.label_folder_path = Path(f"uploads/{self.project_name}/labels")
        self.images_list = [f"{image}" for image in os.listdir(self.image_folder_path)]
        self.labels_list = [f"{label}" for label in os.listdir(self.label_folder_path)]

    def create_record(self):

        self.get_image_label_list()

        self.project_info = {
        "project_name": self.project_name,
        "base_dir_path": "",
        "image_file_paths": self.images_list,
        "label_file_paths": self.labels_list
        }

        self.collections.insert_one(self.project_info)

    def delete_record(self):
        self.collections.delete_one({"project_name": self.project_name})

    def update_record(self):
        pass

    def retrieve_record(self):
        self.result = self.collections.find_one({"project_name": self.project_name})