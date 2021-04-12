import numpy as np
import time
import cv2

image_path = "/home/pi/ball.jpeg"
#Paste the image to be tested path here
label_path = "/home/pi/imagenet_labels.txt"
#Paste the path for the imagenet_labels.txt file"
prototxt_path = "/home/pi/googlenet.prototxt"
#Paste the path for the googlenet.prototxt file"
model_path = "/home/pi/googlenet.caffemodel"
#Paste the path for the googlenet.caffemodel file"

image = cv2.imread(image_path)
rows = open(label_path).read().strip().split("\n")
classes = [r.split(",")[0] for r in rows]

blob = cv2.dnn.blobFromImage(image,1,(224,224),(104,117,123))

print("Loading Model...")
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

net.setInput(blob)
start = time.time()
preds = net.forward()
end = time.time()
print("Classification time: {:.5} seconds".format(end - start))

idxs = np.argsort(preds[0])[::-1][:5]

for(i, idx) in enumerate(idxs):
    if i == 0:
        text = "Label: {}, {:.2f}%".format(classes[idx],preds[0][idx]*100)
        cv2.putText(image, text, (5,25), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        
    print("{}. label: {}, probability: {:.5}".format(i + 1, classes[idx], preds[0][idx]))
    
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
