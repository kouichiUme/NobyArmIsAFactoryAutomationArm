import picamera
import time
camera = picamera.PiCamera() 
camera.start_preview()
time.sleep(10)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()

    
