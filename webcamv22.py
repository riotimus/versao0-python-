import cv2
import time
import numpy as np
import imutils



MODE = "COCO"
#MODE = "MPI"

if MODE is "COCO":
    protoFile = "pose_deploy_linevec.prototxt"
    weightsFile = "pose_iter_440000.caffemodel"
    nPoints = 18
    POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]

elif MODE is "MPI" :
    protoFile = "pose_deploy_linevec_faster_4_stages.prototxt"
    weightsFile = "pose_iter_160000.caffemodel"
    nPoints = 15
    POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]


inWidth = 368
#368
inHeight = 368
threshold = 0.1
#now=datetime.now()
print('dimensions   ',inHeight,inWidth)
input_source = "18 de fevereiro de 2020.mp4"
#input_source = "sample_video.mp4"
#input_source = "8 marco 2020.mp4"
cap = cv2.VideoCapture(input_source)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )
n=10
frames_step = length//n
print('stepssss  ',frames_step)
hasFrame, frame = cap.read()

vid_writer = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame.shape[1],frame.shape[0]))
time1 = time.asctime()

print(time1)
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
'''net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)'''
fames=1
framess=1
while cv2.waitKey(1) < 0:
    t = time.time()
    cap.set(1,frames_step)
    hasFrame, frame = cap.read()
    frameCopy = np.copy(frame)
    if not hasFrame:
        cv2.waitKey()
        break

    time1 = time.asctime()
    print(time1)
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    print(' frames size',frameWidth,'   ',frameHeight)
    scale_percent = 80 # percent of original size
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    time2 = time.asctime()
    print(length,'  ',time2)
    print("blob ", fames,' of   ',length,'  ',time2,' frames size',frameWidth,'   ',frameHeight)
    #time.time())
    
    rgb=frame
    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #rgb = imutils.resize(rgb, width=750)
    #inpBlob = cv2.dnn.blobFromImage(rgb, 1.0, (300, 300), (104.0, 177.0, 123.0))
    #inpBlob = cv2.dnn.blobFromImage(rgb, 1.0, (300, 300), (0, 0, 0))
    #inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),(0, 0, 0), swapRB=False, crop=False)
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),(0, 0, 0))
    
    time2 = time.asctime()
    print('after inpblob       ',time2)
    net.setInput(inpBlob)
    time2 = time.asctime()
    print('after net.setInput  ',time2)
    output = net.forward()
    time2 = time.asctime()
    print('after net.forward   ',time2)
    

    H = output.shape[2]
    W = output.shape[3]
    #fames=fames+1
    fames=fames+frames_step
    framess=framess+1
    print('  frames',fames,'    ',framess)
    # Empty list to store the detected keypoints
    points = []

    for i in range(nPoints):
        # confidence map of corresponding body's part.
        probMap = output[0, i, :, :]
        time2 = time.asctime()
        print('after probmap      ',time2, 'ponto ',i)

        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        time2 = time.asctime()
        print('  after minMaxLoc  ',time2)
        
        # Scale the point to fit on the original image
        x = (frameWidth * point[0]) / W
        y = (frameHeight * point[1]) / H

        if prob > threshold : 
            cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

            # Add the point to the list if the probability is greater than the threshold
            points.append((int(x), int(y)))
        else :
            points.append(None)

    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

        if points[partA] and points[partB]:
            cv2.line(frame, points[partA], points[partB], (0, 255, 255), 3, lineType=cv2.LINE_AA)
            cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.circle(frame, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

    time2 = time.asctime()
    print('after pose pairs  ',time2)
    cv2.putText(frame, "time taken = {:.2f} sec".format(time.time() - t), (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
    # cv2.putText(frame, "OpenPose using OpenCV", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 50, 0), 2, lineType=cv2.LINE_AA)
    # cv2.imshow('Output-Keypoints', frameCopy)
    cv2.imshow('Output-Skeleton', frame)

    vid_writer.write(frame)

vid_writer.release()
