from flask import Flask ,render_template,request,url_for,redirect
from detectdia import Diabetes

app=Flask(__name__)

@app.route("/")
def home1():
	return render_template("home.html")

@app.route("/map")
def map():
	return render_template("map.html")

@app.route("/home2")
def home2():
	return render_template("home2.html")

@app.route("/dd")
def home():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/detect", methods=['GET', 'POST'])
def detect():
	detect=Diabetes()
	if request.method == "POST":
		age = int(request.form["age"])
		bmi = float(request.form["bmi"])
		dpf = float(request.form["dpf"])
		insulin = int(request.form["insulin"])
		skin = int(request.form["skin"])
		bp = int(request.form["bp"])
		glu = int(request.form["glu"])
		try:
			preg = int(request.form["preg"])
		except:
			preg=0
		if(detect.detectf(preg,glu,bp,skin,insulin,bmi,dpf,age)):
			text='Diabetic'
			return render_template("final.html" , value=text)
		text = 'not Diabetic'
		return render_template("final.html", value=text)


if __name__=="__main__":
	app.run()