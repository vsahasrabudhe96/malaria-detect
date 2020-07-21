import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import cv2
from keras.models import load_model
import PIL

model = load_model('model.h5')
print("Model Loaded successfully")

def predict(img_path,model,filename):
    temp = cv2.imread(img_path)
    temp2 = cv2.resize(temp,(64,64),interpolation = cv2.INTER_AREA)
    temp2 = temp2.reshape((-1,64,64,3))
    temp3 = np.array(temp2/255.0)

    pred = model.predict(temp3)
    pred = ['Infected' if pred<0.5 else 'NOT Infected']
    # plt.subplot(1,2,1)
    # plt.imshow(temp)
    # plt.title("Uploaded Image")
    # plt.subplot(1,2,2)
    # plt.imshow(temp)
    # plt.title("Label: {}".format(pred[0]))
    # plt.show()
    #cv2.putText(temp,str(pred[0]),(0,0),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
    cv2.imwrite('./static/predict/{}'.format(filename),temp)
    return pred[0]
