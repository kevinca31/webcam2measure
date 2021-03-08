import cv2
import numpy as np
from PIL import Image
from PIL import ImageStat
import math
from numpy import mean

def brightness(im_file):
    im = Image.open(im_file) #This was Image.open but what was being passed in is an array and can't be used as a file.
    stat = ImageStat.Stat(im)
    gs = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) 
        for r,g,b in im.getdata())
    return sum(gs)/stat.count[0]
    
vidcap = cv2.VideoCapture('output.avi')
success,image = vidcap.read()
count = 0
list_of_brightness = []
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  list_of_brightness.append(brightness("frame%d.jpg" % count))
  print('Read a new frame: ', success)
  count += 1
  
    
overall_avg = mean(list_of_brightness)
for i in range(len(list_of_brightness)):
    print(list_of_brightness[i])
    
print(overall_avg)