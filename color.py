"""
    Compute the most frequent color in all the png images of
    the current directory and create a webpage with a table
    that paints each color
"""    

from PIL import Image
import os


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
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)
    rgb = []
    for i in range(3):
        rgb.append (most_frequent_pixel[1][i])
    trgb = tuple(rgb)
    trgb = '#%02x%02x%02x' % trgb #Transform rgb to Hex color (HTML)
    return trgb

colors = []
for file in os.listdir(os.getcwd()):
    if file.endswith(".png"):
        colors.append(most_frequent(file))
print colors

f = open('colors.html','w')

message = """<html>
<head></head>
<body><p>Most frequent colors in each background or costume images</p>
<table>
  <tr>"""
for i in colors:
    message = message + '<td bgcolor="' + str(i) + '"><font color="' + str(i) + '">....</td>'
message = message + """
  </tr>
</table>

</body>
</html>"""

f.write(message)
f.close()

