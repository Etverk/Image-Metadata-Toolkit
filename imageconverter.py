from PIL import Image 
import os 

file = open('./info.txt')
content = file.readlines()
inputPath = content[3].replace("\n", "")
outputPath = content[4]
print(inputPath, outputPath)


for file in os.listdir(inputPath): 
    if file.endswith(".png"): 
        img = Image.open(inputPath + "\\" + file)
        file_name, file_ext = os.path.splitext(inputPath + "\\" + file)
        print(os.path.splitext(inputPath + "\\" + file))
        print(file_name)
        print(f'{outputPath}\{file.replace(".png", "")}.jpg')
        img.save(f'{outputPath}\{file.replace(".png", "")}.jpg')