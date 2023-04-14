import os
import re
import pytesseract
from PIL import Image

# 配置 Tesseract-OCR 路径
pytesseract.pytesseract.tesseract_cmd = r'E:\SOFT\OCR-tesseract\install\tesseract.exe'

# 定义函数，用于从图片中提取文字
def extract_text_from_image(image_path):
    image = Image.open(image_path)
    # extracted_text = pytesseract.image_to_string(image, lang='chi_sim+eng')
    extracted_text = pytesseract.image_to_string(image, lang='chi_sim')
    return extracted_text

# 定义函数，用于批量处理文件夹中的图片并输出到指定的文本文件中
def extract_text_from_folder(folder_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for filename in os.listdir(folder_path):
            if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
                image_path = os.path.join(folder_path, filename)
                extracted_text = extract_text_from_image(image_path)

                # 将提取的文字写入到文本文件中
                f.write(f'图片 {filename} 的文字：\n')
                f.write(f'{extracted_text}\n\n')
                f.write('***\n\n')

# 指定包含图片的文件夹路径和输出文件路径
folder_path = 'Pictest'
output_file = './outputTXT/result.txt'

# 处理文件夹中的图片并输出到指定的文本文件中
extract_text_from_folder(folder_path, output_file)
