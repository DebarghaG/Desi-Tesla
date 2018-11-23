import picamera
camera = picamera.PiCamera()

def CaptureForTraining:
    i=0
    #250 millisecond delay between images
    #120,000 ms total runtime ( 2 minutes for training)
    while(i<120000)
        timeinms=int((dt.datetime.utcnow() - dt.datetime(1970,1,1)).total_seconds() * 1000)
        camera.capture(‘%s.jpg’, resize=(640, 480), timeinms)
        i+=250
        #Sleeping for 250ms
        sleep(250)

    camera.resolution = (800, 600)