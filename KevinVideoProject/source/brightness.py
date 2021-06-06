import cv2
import numpy as np
from PIL import Image
from PIL import ImageStat
import math
from numpy import mean
from utils import get_dims, get_video_type
#from .utils import "important functions"
def brightness_of_img(im_file):
    im = Image.open(im_file) 
    stat = ImageStat.Stat(im)
    gs = (math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) 
        for r,g,b in im.getdata())
    return sum(gs)/stat.count[0]

def brightness_of_video_stream(num, filename, frames_per_second, res):
    cap = cv2.VideoCapture(num)
    out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))
    success,image = cap.read()
    list_of_brightness_vs = []
    count = 0
    while True:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('frame',frame)
        success,image = cap.read()
        cv2.imwrite("frame%d.jpg" % count, image)
        list_of_brightness_vs.append(brightness_of_img("frame%d.jpg" % count))
        count+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
    overall_avg = mean(list_of_brightness_vs)
    print("brightnesses for a video stream")
    for i in range(len(list_of_brightness_vs)):
        print(list_of_brightness_vs[i])
    print("Overall brightness for video stream: " + str(overall_avg))
    

def brightness_of_video_file(file_name):
    #maybe put a dbug here
    vidcap = cv2.VideoCapture(file_name)
    success,image = vidcap.read()
    list_of_brightness_vf = []
    count = 0
    while success:
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      list_of_brightness_vf.append(brightness_of_img("frame%d.jpg" % count))
      count+=1
      print('Read a new frame: ', success)
    vidcap.release()
    cv2.destroyAllWindows()
    overall_avg = mean(list_of_brightness_vf)
    print("brightnesses given a video input:")
    for i in range(len(list_of_brightness_vf)):
        print(list_of_brightness_vf[i])
        
    print("Overall brightness for video input: " + str(overall_avg))