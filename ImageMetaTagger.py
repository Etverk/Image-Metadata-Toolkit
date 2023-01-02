from exif import Image as ExifImage
from PIL import Image as PillowImage
from PIL import ExifTags
import os
import numpy

file = open('./FinalKeywordList.txt')
content = file.readlines()

keywordsDictionary = {}
for i in range(len(content)):
    keywordsDictionary[f"keywords{i + 1}"] = content[i].replace("\n", "")
print(keywordsDictionary["keywords1"])

imageList = []
file = open('./Information.txt')
content = file.readlines()
imageFolder = (content[7].replace("\n", "")).replace("Import folder: ", "")
exportFolder = (content[8].replace("\n", "")).replace("Export folder: ", "")

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

