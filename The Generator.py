from PIL import Image, ImageDraw, ImageFont
import csv
import os
import arabic_reshaper
from bidi.algorithm import get_display

template_path = 'certificate.png'
csv_path = 'names.csv'
output_folder = 'girls/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

template = Image.open(template_path)

y = 800

font_path = 'arial.ttf' 
font_size = 100
font = ImageFont.truetype(font_path, font_size)


counter = 1


with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name = row[0]  
        reshaped_name = arabic_reshaper.reshape(name)  
        bidi_name = get_display(reshaped_name)  
        certificate = template.copy()
        draw = ImageDraw.Draw(certificate)


        text_width, _ = draw.textsize(bidi_name, font=font)

        center_x = template.width / 2  
        x = center_x - (text_width / 2)


        draw.text((x, y), bidi_name, font=font, fill="black")  


        output_path = output_folder + str(counter) + '_certificate.pdf'
        certificate.save(output_path)


        counter += 1

print("Mission is Done m8!")
