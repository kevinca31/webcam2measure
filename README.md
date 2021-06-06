# webcam2measure
This repository is going to be used to organize multiple files which will be able to get measurements and detail from a webcam.

Outstanding issues:
- The brightness output between the video file and video stream is slightly different
- JUST SO YOU KNOW: the video file method will be printing images to your machine. This is done through the .write() method. The code breaks if this method is not in the code and says FileNotFoundError: [Errno 2] No such file or directory: 'frame0.jpg'
