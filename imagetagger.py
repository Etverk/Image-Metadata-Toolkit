from exif import Image as ExifImage
from PIL import Image as PillowImage
from PIL import ExifTags
import os

# https://blog.matthewgove.com/2022/05/13/how-to-bulk-edit-your-photos-exif-data-with-10-lines-of-python/

imageList = []
file = open('./info.txt')
content = file.readlines()
imageFolder = content[5].replace("\n", "")

for file in os.listdir(imageFolder): 
    imageList.append(file)
    
PILLOW_TAGS = [
    271,    # Camera Make
    272,    # Camera Model
    36867,  # Date/Time Photo Taken
    34853,  # GPS Info
]

EXIF_TAGS = [
    "make",
    "model",
    "datetime_original",
    "gps_latitude",
    "gps_latitude_ref",
    "gps_longitude",
    "gps_longitude_ref",
    "gps_altitude",
]

for img in imageList:
    image_path = f"{imageFolder}\{img}"
    with open(image_path, "rb") as input_file:
        img = ExifImage(input_file)

    if img.has_exif:
        for tag in EXIF_TAGS:
            value = img.get(tag)
            print(f"{tag}: {value}")
            
            
            
            
PILLOW_TAGS = [
    315,     # Artist Name
    33432,   # Copyright Message
]

EXIF_TAGS = [
    "artist",
    "copyright",
]

VALUES = [
    "Matthew Gove",    # Artist Name
    "Copyright 2022 Matthew Gove. All Rights Reserved."  # Copyright Message
]


for img in imageList:
    image_path = f"{imageFolder}\{img}"
    pillow_image = PillowImage.open(image_path)
    img_exif = pillow_image.getexif()

    for tag, value in zip(PILLOW_TAGS, VALUES):
        img_exif[tag] = value

    output_file = img
    pillow_image.save(output_file, exif=img_exif)