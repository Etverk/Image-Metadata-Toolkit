from exif import Image as ExifImage
from PIL import Image as PillowImage
from dotenv import load_dotenv
from PIL import ExifTags
import os
import numpy

file = open('./KeywordList.txt')
content = file.readlines()

keywordsDictionary = {}
for i in range(len(content)):
    keywordsDictionary[f"keywords{i + 1}"] = content[i].replace("\n", "")
print(keywordsDictionary["keywords1"])

load_dotenv() 
imageFolder = os.getenv("ImageMetaTaggerImportFolder")
exportFolder = os.getenv("ImageMetaTaggerExportFolder")

imageList = []
for file in os.listdir(imageFolder): 
    imageList.append(file)

for img in imageList:
    image = PillowImage.open(f"{imageFolder}\{img}")

    XPKeywords = 0x9C9E
    XPTitle = 0x9C9B
    exifdata = image.getexif()
    
    keywordsNumber = (((img[0] + img[1] + img[2]).replace(" ", "")).replace("(", "")).replace(".", "")
    keywordsName = f"keywordsDictionary[\"keywords{keywordsNumber}\"]"
    execString = f"exifdata[XPKeywords] = {keywordsName}.encode(\"utf16\")"
    exec(execString)
    exifdata[XPTitle] = " - Generative AI".encode("utf16")
    print(execString, exportFolder + "\\" + img, exifdata)

    image.save(exportFolder + "\\" + img, exif=exifdata)