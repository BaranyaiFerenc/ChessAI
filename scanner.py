from PIL import Image

FEN_Code = {
    "Black_Rook":"r",
    "Black_Knigth":"n",
    "Black_Bishop":"b",
    "Black_Queen":"q",
    "Black_King":"k",
    "Black_Pawn":"p",

    "White_Rook":"R",
    "White_Knigth":"N",
    "White_Bishop":"B",
    "White_Queen":"Q",
    "White_King":"K",
    "White_Pawn":"P"
}



def CheckColor(color1, color2, threshold = 2):
    return abs(color1[0]-color2[0]) < threshold and abs(color1[1]-color2[1]) < threshold and abs(color1[2] - color2[2]) < threshold



def ClearImage(img, white, black):
    pixels = img.load()
    size = img.size[0]

    for x in range(0,size):
        for y in range(0,size):
            if CheckColor(pixels[x,y], black,15) or CheckColor(pixels[x,y], (185,202,67,255),10):
                pixels[x,y] = white


def CompareImage(img1, img2):
    pix1 = img1.load()
    pix2 = img2.load()

    wrong = 0

    tileSize = img1.size[0]

    for x in range(0,tileSize):
        for y in range(0,tileSize):
            if not CheckColor(pix1[x,y], pix2[x,y],10):
                wrong+=1

    diff = wrong/(tileSize*tileSize)
    return diff


def PrintBoard(tiles, dict):
    for x in range(0,8):
        print(34*'-')
        for y in range(0,8):
            name = "none"
            for i in dict.keys():
                if CompareImage(dict[i], tiles[x*8+y].image) < 0.2:
                    name = i

            print('| '+name,end='')
        print(' |')

    print(34*'-')


def CreateFEN(tiles, dict, fen):
    fenCode = ""
    for x in range(0,8):
        noneCounter = 0
        for y in range(0,8):
            name = "none"
            for i in dict.keys():
                if CompareImage(dict[i], tiles[x*8+y].image) < 0.2:
                    name = i

            if name == "none":
                noneCounter+=1
            else:
                if noneCounter > 0:
                    fenCode+=str(noneCounter)
                    noneCounter = 0
                fenCode+=fen[name]

        if noneCounter >0:
            fenCode+=str(noneCounter)
        if x != 7:
            fenCode += "/"

    return fenCode


class Tile:
    topLeftCorner = (0,0)
    bottomRightCorner = (0,0)

    tileSize = 0

    tileName = "a1"

    blackColor = (0,0,0,255)
    whiteColor = (255,255,255,255)

    fig = 0 #0: empty, 1-10: white figures, 11-20: Black figures

    image = 0

 


def run_scanner(img_path):
    im = Image.open(img_path)
    pix = im.load()
    print(im.size)
    print(pix[100,30])

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


    x2 = 0
    y2 = 0

    while not CheckColor(pix[x2,y2], white) and not CheckColor(pix[x2,y2], black):

        if y2 < im.size[1]-1:
            y2+=1
        elif y2 >= im.size[1]-1:
            y2 = 0
            x2+=1


    topLeft = (x2,y1)


    x1 = im.size[0]-1
    y1 = im.size[1]-1

    while not CheckColor(pix[x1,y1], white) and not CheckColor(pix[x1,y1], black):

        if x1 > 0:
            x1-=1
        elif x1 == 0:
            x1 = im.size[0]-1
            y1-=1


    x2 = im.size[0]-1
    y2 = im.size[1]-1

    while not CheckColor(pix[x2,y2], white) and not CheckColor(pix[x2,y2], black):

        if y2 > 0:
            y2-=1
        elif y2 == 0:
            y2 = im.size[1]-1
            x2-=1

    bottomRight = (x2,y1)


    squareSize = round((bottomRight[0]-topLeft[0])/8)
    print("Size of square: "+str(squareSize))

    tileList = []

    for i in range(0,8):
        for k in range(0,8):
            tile = Tile()
            tile.topLeftCorner = (k*squareSize, i*squareSize)
            tile.tileSize = squareSize
            tile.tileName = (chr(ord('a')+k))+str(8-i)
            tileList.append(tile)

    counter = 0
    for i in tileList:
        tileImg  = Image.new( mode = "RGB", size = (squareSize, squareSize) )
        tilePix = tileImg.load()
        for x in range(0,squareSize):
            for y in range(0,squareSize):
                tilePix[x,y] = pix[topLeft[0]+i.topLeftCorner[0]+x,topLeft[1]+i.topLeftCorner[1]+y]

        base_width = 50
        wpercent = (base_width / float(tileImg.size[0]))
        hsize = int((float(tileImg.size[1]) * float(wpercent)))
        tileImg = tileImg.resize((base_width, hsize), Image.Resampling.LANCZOS)

        ClearImage(tileImg, white, black)
        i.image = tileImg

        for x in range(0,squareSize):
            pix[topLeft[0]+i.topLeftCorner[0]+x, topLeft[1]+i.topLeftCorner[1]] = (255,0,255,255)
            pix[topLeft[0]+i.topLeftCorner[0], topLeft[1]+i.topLeftCorner[1]+x] = (255,0,255,255)

        counter += 1

    CompareImage(tileList[33].image, tileList[57].image)
    '''
    tileList[0].image.save('source/tiles/Black_Rook.png')
    tileList[1].image.save('source/tiles/Black_Knigth.png')
    tileList[2].image.save('source/tiles/Black_Bishop.png')
    tileList[3].image.save('source/tiles/Black_Queen.png')
    tileList[4].image.save('source/tiles/Black_King.png')
    tileList[8].image.save('source/tiles/Black_Pawn.png')


    tileList[56].image.save('source/tiles/White_Rook.png')
    tileList[57].image.save('source/tiles/White_Knigth.png')
    tileList[58].image.save('source/tiles/White_Bishop.png')
    tileList[59].image.save('source/tiles/White_Queen.png')
    tileList[60].image.save('source/tiles/White_King.png')
    tileList[54].image.save('source/tiles/White_Pawn.png')'''

    pieces = {
        "Black_Rook" : Image.open('source/tiles/Black_Rook.png'),
        "Black_Knigth" : Image.open('source/tiles/Black_Knigth.png'),
        "Black_Bishop": Image.open('source/tiles/Black_Bishop.png'),
        "Black_Queen" : Image.open('source/tiles/Black_Queen.png'),
        "Black_King" : Image.open('source/tiles/Black_King.png'),
        "Black_Pawn" : Image.open('source/tiles/Black_Pawn.png'),

        "White_Rook" : Image.open('source/tiles/White_Rook.png'),
        "White_Knigth" : Image.open('source/tiles/White_Knigth.png'),
        "White_Bishop" : Image.open('source/tiles/White_Bishop.png'),
        "White_Queen" : Image.open('source/tiles/White_Queen.png'),
        "White_King" : Image.open('source/tiles/White_King.png'),
        "White_Pawn" : Image.open('source/tiles/White_Pawn.png')
    }



    #PrintBoard(tileList, pieces)

    return CreateFEN(tileList, pieces, FEN_Code)


            