from flask import Flask, request, jsonify
import pandas as pd
import joblib

model = joblib.load('random_forest_model.joblib')
scaler = joblib.load('scaler.joblib')

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def predict() :
    if request.method == 'POST' :
        try :
            data = request.get_json()
            data_df = pd.DataFrame([data])
            scaled_data = scaler.transform(data_df)
            prediction = model.predict(scaled_data)
            return jsonify({'prediction' : prediction.tolist()})
        except Exception as e :
            return jsonify({'error' : str(e)}), 400

if __name__ == '__main__' :
    app.run(debug = True, host = '0.0.0.0', port = 5000)
