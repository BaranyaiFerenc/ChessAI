from PIL import Image



def CheckColor(color1, color2, threshold = 2):
    return abs(color1[0]-color2[0]) < threshold and abs(color1[1]-color2[1]) < threshold and abs(color1[2] - color2[2]) < threshold


im = Image.open('source/chess1.png') # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
print(pix[100,30])  # Get the RGBA Value of the a pixel of an image

white = (235, 236, 208, 255)
black = (119, 149, 86, 255)


x1 = 0
y1 = 0

while not CheckColor(pix[x1,y1], white) and not CheckColor(pix[x1,y1], black):

    if x1 < im.size[0]-1:
        x1+=1
    elif x1 >= im.size[0]-1:
        x1 = 0
        y1+=1

pix[x1,y1] = (255,0,0,255)

x2 = 0
y2 = 0

while not CheckColor(pix[x2,y2], white) and not CheckColor(pix[x2,y2], black):

    if y2 < im.size[1]-1:
        y2+=1
    elif y2 >= im.size[1]-1:
        y2 = 0
        x2+=1

pix[x2,y2] = (255,0,0,255)


pix[x2,y1] = (255,0,0,255)

topLeft = (x2,y1)


x1 = im.size[0]-1
y1 = im.size[1]-1

while not CheckColor(pix[x1,y1], white) and not CheckColor(pix[x1,y1], black):

    if x1 > 0:
        x1-=1
    elif x1 == 0:
        x1 = im.size[0]-1
        y1-=1

pix[x1,y1] = (255,0,0,255)

x2 = im.size[0]-1
y2 = im.size[1]-1

while not CheckColor(pix[x2,y2], white) and not CheckColor(pix[x2,y2], black):

    if y2 > 0:
        y2-=1
    elif y2 == 0:
        y2 = im.size[1]-1
        x2-=1

pix[x2,y2] = (255,0,0,255)


pix[x2,y1] = (255,0,0,255)

bottomRight = (x2,y1)

for i in range(topLeft[0], bottomRight[0]):
    pix[i, topLeft[1]] = (255,0,0,255)
    pix[i, bottomRight[1]] = (255,0,0,255)

for i in range(topLeft[1], bottomRight[1]):
    pix[topLeft[0],i] = (255,0,0,255)
    pix[bottomRight[0],i] = (255,0,0,255)

for x in range(topLeft[0], bottomRight[0]-1):
    for y in range(topLeft[1], bottomRight[1]-1):
        if not CheckColor(pix[x,y], pix[x+1,y],10):
            pix[x,y] = (255,0,0,255)

        if not CheckColor(pix[x,y], pix[x,y+1],10):
            pix[x,y] = (255,0,0,255)

im.save('source/chess1_edited.png')


            