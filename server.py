import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/", methods= ["GET","POST"])
@app.route("/login",  methods=['POST','GET'])
def login():
    return render_template("login.php")

@app.route("/about",  methods=['POST','GET'])
def about():
    return render_template("about.html")

@app.route("/faq",  methods=['POST','GET'])
def faq():
    return render_template("faq.html")

@app.route("/home",  methods=['POST','GET'])
def content():
    if request.method == 'POST':
        Age = request.form['age']
        BMI = request.form['bmi']
        Gender = request.form['gender']
        Smoker = request.form['smoker']
        Location = request.form['location']
        Children = request.form['children']
        data = [[int(Age), float(BMI), int(Gender), int(Smoker), int(Location), int(Children)]]
        with open('mainmodel.pickle','rb') as file:
            model= pickle.load(file)
        print(data)
        predict =model.predict(data)[0]
        print(predict)
        return render_template('result.html', prediction = predict)
    return render_template("content.html" )

if __name__ == '__main__':
    app.run(debug=True)