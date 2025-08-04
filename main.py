import random
import numpy as np
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import matplotlib.pyplot as plt

original_img = Image.open("icon-rounded.png")
new_width, new_height = 150, 150
scaled_img = original_img.resize((new_width, new_height))
pos_x, pos_y = 325, 225

final_img = Image.new('RGB', (800, 600), 'white')
draw = ImageDraw.Draw(final_img)
width, height = final_img.size

for x in range(width):
    for y in range(height):
        r = int((x / width) * 255)
        g = int((y / height) * 255)
        b = 100
        final_img.putpixel((x, y), (r, g, b))

for i in range(150):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.ellipse([x, y, x + 1, y + 1], fill=color)

def hexagon_points(center_x, center_y, size, rotation_degrees=0):
    points = []
    for angle in range(0, 360, 60):
        rad = math.radians(angle + rotation_degrees)
        x = center_x + size * math.cos(rad)
        y = center_y + size * math.sin(rad)
        points.append((x, y))
    return points

def draw_hex_grid(image, hex_size, rows, cols, rotationdeg, offset_x=0, offset_y=0):
    draw = ImageDraw.Draw(image)
    vert_dist = hex_size * 1.5
    horiz_dist = math.sqrt(3) * hex_size

    for row in range(rows):
        for col in range(cols):
            base_x = horiz_dist * col + (horiz_dist / 2 if row % 2 else 0)
            base_y = vert_dist * row
            offset_center_x = base_x + offset_x
            offset_center_y = base_y + offset_y
            hex_points = hexagon_points(offset_center_x, offset_center_y, hex_size, rotation_degrees=rotationdeg)
            draw.polygon(hex_points, outline="black", fill=None)

hex_size = 30
rows = int(height / (hex_size * 1.5)) + 2
cols = int(width / (math.sqrt(3) * hex_size)) + 2

draw_hex_grid(final_img, hex_size, rows, cols, 100, offset_x=0, offset_y=0)
draw_hex_grid(final_img, hex_size, rows, cols, 0, offset_x=hex_size * 1.5, offset_y=hex_size * 1.0)
draw_hex_grid(final_img, hex_size, rows, cols, 0, offset_x=hex_size * 2.5, offset_y=hex_size * 2.0)
draw_hex_grid(final_img, hex_size, rows, cols, 0, offset_x=hex_size * 5.5, offset_y=hex_size * 5.0)

final_img = final_img.filter(ImageFilter.BLUR)
final_img.paste(scaled_img, (pos_x, pos_y), scaled_img.convert('RGBA'))

draw = ImageDraw.Draw(final_img)

font_size = 30
font = ImageFont.truetype("04B_03__.TTF", font_size)
draw.text((210, 500), "Illustrated by Ian Tawileh", fill='white', font=font)

plt.figure(figsize=(12, 9))
plt.imshow(final_img)
plt.axis('off')
plt.title("My Hack Club Iframe Submission - Ready for the Wall!")
plt.show()

print("🎉 Your artwork is ready to be framed and hung at Hack Club HQ!")
