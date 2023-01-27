from PIL import Image as im
import random
import sys

im1 = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\out1.jpg") # image 1
im2 = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\out2.jpg") # image 2
im3 = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\out3.jpg") # image 3

im1 = im1.convert('1')
im2 = im2.convert('1')
im3 = im3.convert('1')

hlf_tn1 = im.new("CMYK", [dmn for dmn in im1.size]) # half-tone image 1 
hlf_tn2 = im.new("CMYK", [dmn for dmn in im1.size]) # half-tone image 2
hlf_tn3 = im.new("CMYK", [dmn for dmn in im1.size]) # half-tone image 3

for i in range(0, im1.size[0]):      # reconstructing half-tone image 
    for j in range(0, im1.size[1]):
        pxl_clr1 = im1.getpixel((i, j))
        pxl_clr2 = im2.getpixel((i, j))
        pxl_clr3 = im3.getpixel((i, j))

        if pxl_clr1 == 255:
            hlf_tn1.putpixel((i, j),(255,0,0,0))
        else:
            hlf_tn1.putpixel((i, j),(0,0,0,0))

        if pxl_clr2 == 255:
            hlf_tn2.putpixel((i, j),(0,255,0,0))
        else:
            hlf_tn2.putpixel((i, j),(0,0,0,0))

        if pxl_clr3 == 255:
            hlf_tn3.putpixel((i, j),(0,0,255,0))
        else:
            hlf_tn3.putpixel((i, j),(0,0,0,0))



hlf_tn1.save('D:\Monsoon 2022- 4\Crypto_gpy\proj\hf1.jpg')
hlf_tn2.save('D:\Monsoon 2022- 4\Crypto_gpy\proj\hf2.jpg')
hlf_tn3.save('D:\Monsoon 2022- 4\Crypto_gpy\proj\hf3.jpg')
