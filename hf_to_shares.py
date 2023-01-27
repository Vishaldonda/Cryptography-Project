from PIL import Image as im
import random
import sys


im1 = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\hf1.jpg")  
im1 = im1.convert('CMYK')

im2 = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\hf2.jpg")
im2 = im2.convert('CMYK')

im3 = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\hf3.jpg")
im3 = im3.convert('CMYK')


shr1 = im.new("CMYK", [dmn * 2 for dmn in im1.size])

shr2 = im.new("CMYK", [dmn * 2 for dmn in im2.size])

shr3 = im.new("CMYK", [dmn * 2 for dmn in im3.size])




for i in range(0, im1.size[0]):
    for j in range(0, im1.size[1]):
        pxlclr = im1.getpixel((i, j))

        if pxlclr[0]+pxlclr[1]+pxlclr[2] == 0:
            shr1.putpixel((i * 2, j * 2), (255,0,0,0))
            shr1.putpixel((i * 2 + 1, j * 2), (0,0,0,0))
            shr1.putpixel((i * 2, j * 2 + 1), (0,0,0,0))
            shr1.putpixel((i * 2 + 1, j * 2 + 1), (255,0,0,0))

        else:
            shr1.putpixel((i * 2, j * 2), (0,0,0,0))
            shr1.putpixel((i * 2 + 1, j * 2), (255,0,0,0))
            shr1.putpixel((i * 2, j * 2 + 1), (255,0,0,0))
            shr1.putpixel((i * 2 + 1, j * 2 + 1), (0,0,0,0))

        pxlclr = im2.getpixel((i, j))

        if pxlclr[0]+pxlclr[1]+pxlclr[2] == 0:
            shr2.putpixel((i * 2, j * 2), (0,255,0,0))
            shr2.putpixel((i * 2 + 1, j * 2), (0,0,0,0))
            shr2.putpixel((i * 2, j * 2 + 1), (0,0,0,0))
            shr2.putpixel((i * 2 + 1, j * 2 + 1), (0,255,0,0))

        else:
            shr2.putpixel((i * 2, j * 2), (0,0,0,0))
            shr2.putpixel((i * 2 + 1, j * 2), (0,255,0,0))
            shr2.putpixel((i * 2, j * 2 + 1), (0,255,0,0))
            shr2.putpixel((i * 2 + 1, j * 2 + 1), (0,0,0,0))

        pxlclr = im3.getpixel((i, j))

        if pxlclr[0]+pxlclr[1]+pxlclr[2] == 0:
            shr3.putpixel((i * 2, j * 2), (0,0,255,0))
            shr3.putpixel((i * 2 + 1, j * 2), (0,0,0,0))
            shr3.putpixel((i * 2, j * 2 + 1), (0,0,0,0))
            shr3.putpixel((i * 2 + 1, j * 2 + 1), (0,0,255,0))

        else:
            shr3.putpixel((i * 2, j * 2), (0,0,0,0))
            shr3.putpixel((i * 2 + 1, j * 2), (0,0,255,0))
            shr3.putpixel((i * 2, j * 2 + 1), (0,0,255,0))
            shr3.putpixel((i * 2 + 1, j * 2 + 1), (0,0,0,0))



shr1.save('D:\Monsoon 2022- 4\Crypto_gpy\proj\share1.jpg')
shr2.save('D:\Monsoon 2022- 4\Crypto_gpy\proj\share2.jpg')
shr3.save('D:\Monsoon 2022- 4\Crypto_gpy\proj\share3.jpg')
