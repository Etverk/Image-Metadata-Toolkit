from PIL import Image 
import os 

inputFormat = "png"
outputFormat = "jpg"

file = open('./info.txt')
content = file.readlines()
inputPath = content[3].replace("\n", "")
outputPath = content[4].replace("\n", "")
print(inputPath, outputPath)

for file in os.listdir(inputPath): 
    if file.endswith(f".{inputFormat}"): 
        img = Image.open(inputPath + "\\" + file)
        file_name, file_ext = os.path.splitext(inputPath + "\\" + file)
        print(os.path.splitext(inputPath + "\\" + file))
        print(file_name)
        print(f'{outputPath}\{file.replace(f".{inputFormat}", "")}.{outputFormat}')
        img.save(f'{outputPath}\{file.replace(f".{inputFormat}", "")}.{outputFormat}')