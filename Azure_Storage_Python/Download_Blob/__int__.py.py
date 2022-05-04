import pandas as pd
from azure.storage.blob import BlobServiceClient 
import os



constrin = "<connection string to Azure Storage>"

connection_string = constrin
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(r"<path to the blob in storage>")
File_Name = container_client.get_blob_client("<blob/file name>")


blob = File_Name.download_blob().readall().decode("utf-8") #decode depends on the type of file. utf is for csv file.


file_name = "<blob/file name>" 
path = "."  #path where you want to download the file

download_file_path = os.path.join(path,file_name ) #Create the path for file download


with open(download_file_path , "wb") as download_file:   # downloads the blob
    download_file.write(File_Name.download_blob().readall())  

