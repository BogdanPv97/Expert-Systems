import numpy as np
import PIL
from PIL import Image
import csv
from csv import DictReader

color_mapping = [];
diff = 2

with open('colors.csv', 'r') as read_obj:
    dict_reader = DictReader(read_obj)
    color_temp = list(dict_reader)
    color_mapping = color_temp

color_mapping_size = len(color_mapping);


def open_image(path):
    newImage = Image.open(path)
    return newImage

def getPixel(image, i, j):
    width, height = image.size
    if i > height or j > width:
        return None

    pixel = image.getpixel((j, i))
    return pixel


def find_Color(i, j, max_difference, red, green, blue):
    for x in range(color_mapping_size):
        if red >= int(color_mapping[x]['red']) - max_difference and red <= int(
                color_mapping[x]['red']) + max_difference and green >= int(
                color_mapping[x]['green']) - max_difference and green <= int(
                color_mapping[x]['green']) + max_difference and blue >= int(
                color_mapping[x]['blue']) - max_difference and blue <= int(color_mapping[x]['blue']) + max_difference:
           
            return color_mapping[x]['name'] + ' (' + color_mapping[x]['red'] + ',' + color_mapping[x]['green'] + ',' + \
                   color_mapping[x]['blue'] + ')'
           
    return find_Color(i, j, max_difference +diff, red, green, blue)


def image_pixels(image):
    height = image.height
    width = image.width

    for i in range(height):
        for j in range(width):
            pixel = getPixel(image, i, j)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            print("\nPixel", i, j, "with", "red", red, "green", green, "blue", blue, sep=" ")
            print("Pixel color:")
            print(find_Color(i, j, diff, red, green, blue));


image = open_image("image.jpg")




def write_to_CSV(image) -> object:
    with open('pixelColor.csv', 'w', newline='') as csvOut:
        header = ['imageX', 'imageY', 'RGB Pixel Code', 'Color']
        w = csv.DictWriter(csvOut, fieldnames=header)
        w.writeheader();

        height = image.height
        width = image.width

        for i in range(height):
            for j in range(width):
                pixel = getPixel(image, i, j)

                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]

                w.writerow({
                    'imageX': i,
                    'imageY': j,
                    'RGB Pixel Code': '(' + str(red) + ',' + str(green) + ',' + str(blue) + ')',
                    'Color': find_Color(i, j, diff, red, green, blue)

                })
write_to_CSV(image)
#Each pixel color cand e found in the csv file
