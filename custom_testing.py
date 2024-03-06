import torch
from easyocr import Reader


reader = Reader(['en', 'bn'], recog_network='custom_example')
result = reader.readtext("/home/bipin/projects/EasyOCR/trainer/all_data/train/18552.jpg", detail=0)
output_file_path = "/home/bipin/projects/EasyOCR/trainer/ocr_result.txt"

# Write the result to a text file
with open(output_file_path, "w") as file:
    for text in result:
        file.write(text + "\n")
