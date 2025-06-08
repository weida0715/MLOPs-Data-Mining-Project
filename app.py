from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the saved model pipeline
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        # Get form values
        data = {
            "age": float(request.form["age"]),
            "num_brought_up_children": int(request.form["num_brought_up_children"]),
            "religiosity": int(request.form["religiosity"]),
            "safety": int(request.form["safety"]),
            "love": int(request.form["love"]),
            "globe": int(request.form["globe"])
        }

        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]

    return render_template("marital_satisfaction.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=False)
