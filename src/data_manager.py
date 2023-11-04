import os
from pathlib import Path
import pymongo
# import json
# import glob

class Data_Manager:
    def __init__(self, project_name):
        self.project_name = project_name
        
        self.create_mongo_connection()
        self.operate_mongo_db()
        
        
    # Making operation on mongo db to retrieve information
    
    def operate_mongo_db(self):
        

        # self.json_file_path = Path(f"data/{self.project_name}/{self.project_name}.json")

        # if Path.exists(self.json_file_path):
        #     with open(f"{self.json_file_path}", 'r') as json_file:
        #         return json.load(json_file)
        self.retrieve_record()

        if self.result is not None:
            self.project_info = self.result
            print(f"Number of Images: {self.result['num_images']} \nNumber of Labels: {self.result['num_labels']}")
            return
        
        self.create_record()

        # with open(self.json_file_path, 'w') as json_file:
        #     json.dump(project_info, json_file)
    
    # Creating database with MongoDB
    def create_mongo_connection(self):
        
        try:
            client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
            self.mydb = client['ALL_Data_Management']
            self.collections = self.mydb.all_data_managementinformations  
        
        except Exception as e:
            print(e)
    
    def get_image_label_list(self):
        self.image_folder_path = Path(f"data/{self.project_name}/images")
        self.label_folder_path = Path(f"data/{self.project_name}/labels")
        self.images_list = [f"{image}" for image in os.listdir(self.image_folder_path)]
        self.labels_list = [f"{label}" for label in os.listdir(self.label_folder_path)]

    def create_record(self):

        self.get_image_label_list()

        self.project_info = {
        "project_name": self.project_name,
        "base_dir_path": "ALL_Data_Management/data",
        "num_images": len(self.images_list),
        "num_labels": len(self.labels_list),
        "image_folder_path": str(self.image_folder_path),
        "label_folder_path": str(self.label_folder_path),
        "image_file_paths": self.images_list,
        "label_file_paths": self.labels_list
        }

        self.collections.insert_one(self.project_info)

    def delete_record(self):
        pass

    def update_record(self):
        pass

    def retrieve_record(self):
        self.result = self.collections.find_one({"project_name": self.project_name})