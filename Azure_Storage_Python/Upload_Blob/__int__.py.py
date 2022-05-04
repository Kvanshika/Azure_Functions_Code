from azure.storage.blob import BlobServiceClient 


constrin = "<connection string to Azure Storage>"


blob = BlobClient.from_connection_string(conn_str=  constrin, container_name = r"<container_name>", blob_name = "<blob_name>")

with open("./FileName.txt", "rb") as data:
    blob.upload_blob(data)
