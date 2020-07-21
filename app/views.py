from flask import render_template, request
from flask import redirect, url_for
import os
from PIL import Image
from utils import predict
from tensorflow.keras.models import load_model
model = load_model('./model/model.h5')

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