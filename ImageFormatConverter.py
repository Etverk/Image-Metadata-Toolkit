from PIL import Image 
import os 

file = open('./Information.txt')
content = file.readlines()
inputFormat = (content[11].replace("\n", "")).replace("Input format: ", "")
outputFormat = (content[12].replace("\n", "")).replace("Output format: ", "")
inputPath = (content[13].replace("\n", "")).replace("Import folder path: ", "")
outputPath = (content[14].replace("\n", "")).replace("Export folder path: ", "")

for file in os.listdir(inputPath): 
    if file.endswith(f".{inputFormat}"): 
        img = Image.open(inputPath + "\\" + file)
        file_name, file_ext = os.path.splitext(inputPath + "\\" + file)
        print(os.path.splitext(inputPath + "\\" + file))
        print(file_name)
        print(f'{outputPath}\{file.replace(f".{inputFormat}", "")}.{outputFormat}')
        img.save(f'{outputPath}\{file.replace(f".{inputFormat}", "")}.{outputFormat}')