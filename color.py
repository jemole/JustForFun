"""
    Compute the most frequent color in all the png images of
    the current directory and create a webpage with a table
    that paints each color
"""    

from PIL import Image
import os
import webcolors
from collections import Counter

def getKey(item):
    """
        Used to sort the list of files and colors
    """
    return item[0]

def blackOrWhite(color):
    """
        Check if color is black (1) or white (2) or otherwise (0)
    """
    if (color[0] == 255 and color[1] == 255 and color [2] == 255):
        return 1
    elif (color[0] == 0 and color[1] == 0 and color [2] == 0):
        return 2
    return 0

def warmOrCool(rgb):
    """
        Check if color is warm or cool 
    """
    if rgb[0] > rgb[2]:
        return "Warm"
    else:
        return "Cool"

def closest_colour(requested_colour):
    """
        Return the name of the closest color
    """
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    """
        Return the name of the color
    """
    try:
        closest_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
    return closest_name

def most_frequent(img):
    """
        Compute the most frequent color in img.
        Code adapted from 
        http://blog.zeevgilovitz.com/detecting-dominant-colours-in-python/
    """
    image = Image.open(img)
    w, h = image.size
    pixels = image.getcolors(w * h)
    most_frequent_pixel = pixels[0]
    for count, colour in pixels:
        if not blackOrWhite(colour):
            if count > most_frequent_pixel[0]:
                most_frequent_pixel = (count, colour)
    rgb = []
    for i in range(3):
        rgb.append (most_frequent_pixel[1][i])
    return tuple(rgb)
    #trgb = '#%02x%02x%02x' % trgb #Transform rgb to Hex color (HTML)
    #return trgb

colors = []
element = []
for file in os.listdir(os.getcwd()):
    if file.endswith(".png"):
        element.append(str(file))
        #element.append(most_frequent(file))
        mf = most_frequent(file)
        element.append('#%02x%02x%02x' % mf)
        element.append(warmOrCool(mf))
        element.append(get_colour_name(mf))
        colors.append(element)
        element = []
#print colors

f = open('colors.html','w')

message = """<html>
<head></head>
<body><p>Most frequent colors in each background or costume images</p>
<table>
  <tr>"""
for i in sorted(colors, key=getKey):
    message = message + '<td><small>' + str(i[0]) + '</small></td>'
message = message + """
  </tr>
  <tr>"""
for i in sorted(colors, key=getKey):
    message = message + '<td bgcolor="' + str(i[1]) + '"><font color="' + str(i[1]) + '">.....</td>'
message = message + """
  </tr>
  <tr>"""
for i in sorted(colors, key=getKey):
    message = message + '<td><small>' + str(i[2]) + '</small></td>'
message = message + """
  </tr>"""
for i in sorted(colors, key=getKey):
    message = message + '<td><small>' + str(i[3]) + '</small></td>'
message = message + """
  </tr>
</table>
<br>"""
warm = 0
cool = 0

for i in colors:
    if i[2] == "Warm":
        warm += 1
    else:
        cool += 1
message = message + '<p><small>Number of pictures with warm color: ' + str(warm) + '</small></p>'
message = message + '<p><small>Number of pictures with cool color: ' + str(cool) + '</small></p>'

colorList = [x[3] for x in colors]
color_counts = Counter(colorList)

message = message + '<p><small>Most common colors: ' + str(color_counts.most_common(3)) + '</small></p>'

message = message + """
</body>
</html>"""

f.write(message)
f.close()

