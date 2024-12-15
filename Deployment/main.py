from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import requests


app = Flask(__name__)

@app.route('/', methods = ['GET']) 
def index() :
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST' :
        url = 'http://127.0.0.1:5000'
        try :
            inches = float(request.form['inches'])
            ram = int(request.form['ram'])
            weight = float(request.form['weight'])
            screen_width = int(request.form['width'])
            screen_height = int(request.form['height'])
            frequency = float(request.form['frequency'])
            memory_size = float(request.form['size'])
        except ValueError :
            return render_template('index.html', prediction = "Invalid input. Please enter valid numbers.")
        
        given_data = {
            'Inches' : inches,
            'Ram' : ram,
            'Weight' : weight,
            'Screen_width' : screen_width,
            'Screen_height' : screen_height,
            'Frequency' : frequency,
            'Memory_size' : memory_size
        }

        try :
            response = requests.post(f'{url}/', json = given_data)
            if response.status_code != 200 :
                return render_template('index.html', prediction = f"Error from API : {response.text}")
            
            prediction = response.json().get('prediction', 'No prediction returned')
            if isinstance(prediction, list) and len(prediction) > 0:
                prediction = f'{prediction[0]:.2f}'

            return render_template('index.html', prediction = prediction)
        
        except Exception as e :
            return jsonify({'error' : str(e)}), 400, {'Content-Type' : 'application/json'}

    return render_template('index.html')

if __name__ == '__main__' :
    app.run(debug = True, port = 8000)