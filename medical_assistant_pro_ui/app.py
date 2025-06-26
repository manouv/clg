from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
users = {"admin": "admin123"}
medical_data = {
    "fever": {"diagnosis": "Viral Fever", "medicines": ["Paracetamol", "Crocin"], "images": ["paracetamol.jpg", "crocin.jpg"]},
    "headache": {"diagnosis": "Tension Headache", "medicines": ["Ibuprofen", "Saridon"], "images": ["ibuprofen.jpg", "saridon.jpg"]},
    "skin rash": {"diagnosis": "Dermatitis", "medicines": ["Cetirizine", "Hydrocortisone Cream"], "images": ["cetirizine.jpg", "hydrocortisone.jpg"]},
    "chest pain": {"diagnosis": "Possible Angina (Heart)", "medicines": ["Aspirin", "Sorbitrate"], "images": ["aspirin.jpg", "sorbitrate.jpg"]}
}
@app.route('/')
def home(): return redirect('/login')
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["username"]
        pwd = request.form["password"]
        if uname in users and users[uname] == pwd:
            return redirect("/index")
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symptom = request.form["symptom"].lower()
        result = medical_data.get(symptom)
        return render_template("result.html", symptom=symptom, result=result)
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
