from PIL import Image as im
import sys

input1 = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\share1.jpg")  #share image 1
input2 = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\share2.jpg")  #share image 2
input3 = im.open("D:\Monsoon 2022- 4\Crypto_gpy\proj\share3.jpg")  #share image 3

output = im.new('CMYK', input1.size)

for i in range(0,input1.size[0],2): # decrypting the share images
    for j in range(0,input1.size[1],2):

        C = input1.getpixel((i+1, j))[0]
        M = input2.getpixel((i+1, j))[1]
        Y = input3.getpixel((i+1, j))[2]


        output.putpixel((i, j), (C,M,Y,0))
        output.putpixel((i+1, j), (C,M,Y,0))
        output.putpixel((i, j+1), (C,M,Y,0))
        output.putpixel((i+1, j+1), (C,M,Y,0))


output.save("D:\\Monsoon 2022- 4\\Crypto_gpy\\proj\\final.jpg")  # final output of the image using decryption
