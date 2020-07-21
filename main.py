from flask import Flask
from app import views

app = Flask(__name__)

# url section
app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/malariaapp','malariaapp',views.malariaapp)
app.add_url_rule('/malariaapp/detect','malariadetect',views.malariadetect, methods=['GET','POST'])



#run section
if __name__== "__main__":
    app.run(debug=True)