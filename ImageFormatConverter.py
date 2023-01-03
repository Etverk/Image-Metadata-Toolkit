from PIL import Image 
from dotenv import load_dotenv
import os 

load_dotenv() 
inputFormat = os.getenv("ImageFormatConverterImportFormat")
outputFormat = os.getenv("ImageFormatConverterExportFormat")
inputPath = os.getenv("ImageFormatConverterImportFolder")
outputPath = os.getenv("ImageFormatConverterExportFolder")

for file in os.listdir(inputPath): 
    if file.endswith(f".{inputFormat}"): 
        img = Image.open(inputPath + "\\" + file)
        file_name, file_ext = os.path.splitext(inputPath + "\\" + file)
        print(os.path.splitext(inputPath + "\\" + file))
        print(file_name)
        print(f'{outputPath}\{file.replace(f".{inputFormat}", "")}.{outputFormat}')
        img.save(f'{outputPath}\{file.replace(f".{inputFormat}", "")}.{outputFormat}')