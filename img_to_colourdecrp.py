from PIL import Image as im

import random
import sys


image = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\color_image.jpg")  
color_image = image.convert('CMYK')
bw_image = image.convert('1')



output1 = im.new("CMYK", [dmn for dmn in image.size])

output2 = im.new("CMYK", [dmn for dmn in image.size])

output3 = im.new("CMYK", [dmn for dmn in image.size])



for i in range(0, image.size[0], 1):  # decomposition of the color image
    for j in range(0, image.size[1], 1):
        sourcepixel = image.getpixel((i, j))

        output1.putpixel((i, j),(sourcepixel[0],0,0,0))

        output2.putpixel((i, j),(0,sourcepixel[1],0,0))

        output3.putpixel((i, j),(0,0,sourcepixel[2],0))


output1.save('D:\Monsoon 2022- 4\Crypto_gpy\proj\out1.jpg')
output2.save('D:\Monsoon 2022- 4\Crypto_gpy\proj\out2.jpg')
output3.save('D:\Monsoon 2022- 4\Crypto_gpy\proj\out3.jpg')
