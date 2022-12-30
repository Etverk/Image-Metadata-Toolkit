from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes, Details
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

file = open('./Data.txt')
content = file.readlines()
subscription_key = content[7].replace("\n", "")
endpoint = content[8].replace("\n", "")

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")

print("===== Describe an Image - local =====")
local_image_path = os.path.join (images_folder, "26 (1).jpg")
local_image = open(local_image_path, "rb")

description_result = computervision_client.describe_image_in_stream(local_image, 10)

print("Description of local image: ")
if (len(description_result.captions) == 0):
    print("No description detected.")
else:
    for caption in description_result.captions:
        print(caption.text.capitalize())
print(description_result.captions)
