
from flask import render_template, request
from flask import redirect, url_for
import os
from PIL import Image
from keras.models import load_model
model = load_model('model.h5')
import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import cv2
model = load_model('model.h5')

print("Model Loaded successfully")

from flask import Flask

app = Flask(__name__)


def predict(img_path,model,filename):
    temp = cv2.imread(img_path)
    temp2 = cv2.resize(temp,(64,64),interpolation = cv2.INTER_AREA)
    temp2 = temp2.reshape((-1,64,64,3))
    temp3 = np.array(temp2/255.0)

    pred = model.predict(temp3)
    pred = ['Infected' if pred<0.5 else 'NOT Infected']
    cv2.imwrite('./static/predict/{}'.format(filename),temp)
    return pred[0]

UPLOAD_FOLDER = 'static/upload'

def base():
    return render_template("base.html")

def index():
    return render_template('index.html')

def malariaapp():
    return render_template('malariaapp.html')

def getwidth(path):
    img = Image.open(path)
    size = img.size
    aspect = size[0]/size[1]
    w = 250*aspect
    return int(w)

def malariadetect():
    if request.method=='POST':
        f = request.files['image']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER,filename)
        f.save(path)

        w = getwidth(path)
        pred = predict(img_path=path,model=model,filename=filename)
        return render_template('malaria.html',fileupload=True,img_name=filename,w=w,prediction_text='The patient is {} with malaria'.format(pred))


    return render_template('malaria.html',fileupload=False,img_name="xyz.png",w=300)

# url section
app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/malariaapp','malariaapp',views.malariaapp)
app.add_url_rule('/malariaapp/detect','malariadetect',views.malariadetect, methods=['GET','POST'])



#run section
if __name__== "__main__":
    app.run(debug=True)
