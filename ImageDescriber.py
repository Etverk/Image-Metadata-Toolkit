from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes, Details
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
import sys
import time

from exif import Image as ExifImage
from PIL import Image as PillowImage
from PIL import ExifTags

file = open('./Information.txt')
content = file.readlines()
subscription_key = (content[17].replace("\n", "")).replace("Subscription key: ", "")
endpoint = (content[18].replace("\n", "")).replace("Endpoint: ", "")
imageFolder = os.path.join (os.path.dirname(os.path.abspath(__file__)), (content[19].replace("\n", "")).replace("Import folder path: ", ""))
exportFolder = (content[20].replace("\n", "")).replace("Export folder path: ", "")

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

imageList = []
for file in os.listdir(imageFolder): 
    imageList.append(file)

for img in imageList:
    print(img)
    
    local_image = open(f"{imageFolder}\{img}", "rb")
    description_result = computervision_client.describe_image_in_stream(local_image, 10)

    if (len(description_result.captions) == 0):
        print(f"No description detected for {img}.")
    else:
        imageDescription = description_result.captions[0].text.capitalize() + " - Generative AI"
    
    image = PillowImage.open(f"{imageFolder}\{img}")
    XPTitle = 0x9C9B
    exifdata = image.getexif()
    
    exifdata[XPTitle] = imageDescription.encode("utf16")
    image.save(exportFolder + "\\" + img, exif=exifdata)