from azure.storage.blob import BlobServiceClient

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

uploadToBlobStorage('C:\\Users\\user\\Documents\\GitHub\\HackUPC2023\\Imgur\\rentalia-medium-devices-spring.jpg', 'image1.jpg')