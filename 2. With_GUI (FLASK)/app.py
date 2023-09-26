from flask import Flask
from flask import render_template , request
import pickle

app = Flask(__name__,template_folder='folder')

@app.route("/")
def home():
	return render_template('sample.html')

@app.route("/check")
def check():
	no_courses = float(request.args.get("nc"))
	ti_std = float(request.args.get("tstd"))
	
	with open("sm.model", "rb") as f:
		model = pickle.load(f)
	
	marks = model.predict([[no_courses, ti_std]])
	m = "Approximatly you will scoure : " + str(marks)
	return render_template("sample.html", m=m)

if __name__ == "__main__":
	app.run(debug = True, use_reloader = True)