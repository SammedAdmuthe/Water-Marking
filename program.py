from PIL import Image, ImageDraw, ImageFont
import numpy
# create Image object with the input image
IMAGE = Image.open('Test3.png')
HEIGHT, WIDTH = IMAGE.size
DATA = list(IMAGE.convert("1").getdata())
ARR = numpy.reshape(DATA, (HEIGHT, -1))
NROWS = HEIGHT
NCOLS = WIDTH
SKIP = 0
AREA_MAX = (0, [])
W = numpy.zeros(dtype=int, shape=ARR.shape)
H = numpy.zeros(dtype=int, shape=ARR.shape)
for r in range(0, NROWS):
    for c in range(0, NCOLS):
        if ARR[r][c] == SKIP:
            continue
        if r == 0:
            H[r][c] = 1
        else:
            H[r][c] = H[r-1][c]+1
        if c == 0:
            W[r][c] = 1
        else:
            W[r][c] = W[r][c-1]+1
        minw = W[r][c]
        for dh in range(H[r][c]):
            minw = min(minw, W[r-dh][c])
            AREA = (dh+1)*minw
            if AREA > AREA_MAX[0]:
                AREA_MAX = (AREA, [(r-dh, c-minw+1, r, c)])
print("WHITE SPACE AREA  = "+str(AREA_MAX[0]))
for t in AREA_MAX[1]:
    print('Cell 1:({}, {}) and Cell 2:({}, {})'.format(*t))
# initialise the drawing context with the image object as background
DRAW = ImageDraw.Draw(IMAGE)
FONT = ImageFont.truetype('OpenSans-Regular.ttf', size=20)
PURPOSE = 'For ICICI Bank'
COLOR = 'rgb(0, 0, 0)' # black color
TEXTSIZE = X1, Y1 = FONT.getsize(PURPOSE)
TEXT_AREA = X1*Y1
print("TEXT AREA REQUIRED " + str(TEXT_AREA))
if AREA_MAX[0] > TEXT_AREA:
    # starting position of the message
    for t in AREA_MAX[1]:
        (X, Y) = (t[0], t[1])
    # draw the message on the background
    DRAW.text((X, Y), PURPOSE, fill=COLOR, font=FONT)
    # save the edited image
    IMAGE.save('output.png')
    print("Image saved")
else:
    #Create white area to be appended
    WHITE_IMAGE = Image.new("RGB", (IMAGE.width, Y1+10), (255, 255, 255))
    #Add puprpose to the white image
    DRAW = ImageDraw.Draw(WHITE_IMAGE)
    DRAW.text((1, 1), PURPOSE, fill=COLOR, font=FONT)
    #Create resultant image by merging both the images
    RESULT = Image.new("RGB", (IMAGE.width, IMAGE.height+IMAGE.height))
    RESULT.paste(IMAGE, (0, 0))
    RESULT.paste(WHITE_IMAGE, (0, IMAGE.height))
    #Display the image
    # image.show()
    #Save image
    RESULT.save("output.png")
    print("Image saved")
