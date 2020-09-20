import cv2
import sys

if (len(sys.argv) != 3):
    print('Usage: python3 convert_video_to_images <PATH TO VIDEO> <PATH TO OUTPUT LOCATION>')
    sys.exit()

vidcap = cv2.VideoCapture(sys.argv[1])

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(sys.argv[2]+"image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
