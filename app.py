from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)


model, encoders = joblib.load("mushroom_model.pkl")

features = [col for col in encoders.keys() if col != 'class']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        input_data = []
        for feature in features:
            val = request.form[feature]
            le = encoders[feature]
            try:
                encoded_val = le.transform([val])[0]
            except ValueError:
                return f"Invalid value '{val}' for feature '{feature}'. Allowed: {list(le.classes_)}"
            input_data.append(encoded_val)

        input_df = pd.DataFrame([input_data], columns=features)
        pred = model.predict(input_df)[0]
        prediction = encoders['class'].inverse_transform([pred])[0]

    return render_template("index.html", features=features, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
