from flask import Flask,render_template,jsonify,request
import config
from Project_.utils import MedicalInsurance
import numpy as np

app = Flask(__name__)

@app.route("/")
def get_home():
    return "WELCOME TO SANDESH API"

@app.route("/predict_charges",methods = ["POST","GET"])
def get_insurance():
    if request.method == "GET":
        data = request.form
        age = int(data["age"])
        Gender = data["Gender"]
        bmi   = float(data['bmi'])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]

        med_obj = MedicalInsurance(age,Gender,bmi,children,smoker,region)
        charges = med_obj.get_predicted_charges()
        return jsonify({"Result":f"Prdeicted Medical Insurance is {np.around(charges[0]),2}"})
    


if __name__=="__main__":
    app.run()


