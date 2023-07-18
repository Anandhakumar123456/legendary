#Date: 14-07-2023
#Day : Friday

"""

#image download and read and write operations

#Method 1: using for loop:

f=open("boy.jpg","rb")
n=open("boy1.jpg","wb")

for i in f:
    n.write(i)


from PIL import Image

# Read image
img = Image.open('boy.jpg')

# Output Images
img.show()

# prints format of image
print(img.format)

# prints mode of image
print(img.mode)



import imageio as iio

# read an image
img = iio.imread("g4g.png")

# write it in a new format
iio.imwrite("g4g.jpg", img)




#download MongoDB and install

"""

f=open("boy.jpg","rb")
n=open("boy4.jpg","wb")

for i in f:
    n.write(i)



