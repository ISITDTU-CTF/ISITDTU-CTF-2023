from PIL import Image, ImageDraw

img_raw = Image.open('raw.png')
pixelsRaw = img_raw.load()

img_chall = Image.open('chall.png')
pixelsEnc = img_chall.load()

flag = ""

for i in range(img_raw.size[0]):
    for j in range(img_raw.size[1]):
        if pixelsRaw[i,j] != pixelsEnc[i,j]:
            c = int(pixelsEnc[i,j][0]) - int(pixelsRaw[i,j][0])
            if c == -1:
                c = 0
            flag += str(c)

img_QR = Image.new('1', (58, 58), color=1) # Background white
draw = ImageDraw.Draw(img_QR)

for h in range(58):
    for w in range(58):
        if flag[h * 58 + w] == '0':
            draw.point((w, h), 0) # Draw black

#img_QR.show()
img_QR.save('QR2.png')

