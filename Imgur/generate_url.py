from azure.storage.blob import BlobServiceClient
from datetime import datetime

storage_account_key = "9ySS1QeMCWCmxhQHynGjmq0fAZ5Nm8S1xTsc1uAA+o+AIxwoZc2qvzxlt65O4HqAgcfAYOdEA/W8+AStbBzmRQ=="
storage_account_name = "hackupc"
connection_string = "DefaultEndpointsProtocol=https;AccountName=hackupc;AccountKey=3lvbS2yJ7x4k5T8buW6fkOu9CCQgToEco100+3yt2mIC9QeIjSvmFlDWPlkqwhcbg3Bec6GIACG8+AStVRnbgA==;EndpointSuffix=core.windows.net"
container_name = "images"

def uploadToBlobStorage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container= container_name, blob= file_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

    print(f"uploaded {file_name} file")

    return blob_client.url



def uploadToBlobStorage2(image, extension):

    now = datetime.now()
    current_time = now.strftime("%Y_%m_%d_t_%H_%M_%S.%f")

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container= container_name, blob= f'image_{current_time}{extension}')

    blob_client.upload_blob(image)

    return blob_client.url

def get_num_of_images_stored():

    # Initialize a BlobServiceClient object with your storage account connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a reference to the container that you want to count the blobs in
    container_client = blob_service_client.get_container_client(container_name)

    # Get the list of all blobs in the container
    blobs_list = container_client.list_blobs()

    # Count the number of blobs in the container
    count = sum(1 for _ in blobs_list)

    return count

def get_urls_of_images_stored():
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blob_urls = []
    blobs = container_client.list_blobs()
    for blob in blobs:
        blob_url = container_client.url + '/' + blob.name
        print(blob_url)
        blob_urls.append(blob_url)

    return blob_urls