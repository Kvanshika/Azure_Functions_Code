import pandas as pd
from azure.storage.blob import BlobServiceClient 
import os



constrin = "<connection string to Azure Storage>"

connection_string = constrin
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(r"<path to the blob in storage>")
File_Name = container_client.get_blob_client("<blob/file name>")


blob = File_Name.download_blob().readall().decode("utf-8") #decode depends on the type of file. utf is for csv file.

data = pd.read_csv(StringIO(blob)) #the file will be accessed and the data will be moved to dataframe and can be used furthera




