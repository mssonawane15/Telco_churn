from flask import Flask,json,request,render_template
from utils import Telco_Customer_Churn
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict",methods = ["POST"])
def Predict():
    data = request.form

    instance = Telco_Customer_Churn(data)
    result = instance.Predict()

    if result =="No":
        return render_template("result.html",data=f"Cutsomer will may discontinue with your service" )
    else:
         return render_template("result.html",data=f"Cutsomer will keep continue with your service" )

   
app.run(debug=True)