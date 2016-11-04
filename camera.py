import cv2
import time

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        #self.video = cv2.VideoCapture('ShAaNiG.mkv')
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        # if not self.video.isOpened():
        #     print "Error"
        frameWidth = int(self.video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
        frameHeight = int(self.video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        cv2.putText(img = image, 
                        text = "Python",
                        org = (int(frameWidth/2 - 300),int(frameHeight/2)), 
                        fontFace = cv2.FONT_HERSHEY_DUPLEX, 
                        fontScale = 6, 
                        color = (255,255,255),
                        thickness = 5, 
                        lineType = cv2.CV_AA)
        #cv2.imwrite("frame%d.jpg" % int(time.time()), image) 
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
