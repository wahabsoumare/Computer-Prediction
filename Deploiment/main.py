from flask import Flask, request, render_template
import pandas as pd
import joblib

model = joblib.load('random_forest_model.joblib')
scaler = joblib.load('scaler.joblib')

app = Flask(__name__)

@app.route('/', methods = ['GET']) 
def index() :
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict() :
    if request.method == 'POST' :
        try :
            inches = float(request.form['inches'])
            ram = int(request.form['ram'])
            weight = float(request.form['weight'])
            screen_width = int(request.form['width'])
            screen_height = int(request.form['height'])
            frequency = float(request.form['frequency'])
            memory_size = float(request.form['size']) * 1024  # Conversion Go en Mo
            company = int(request.form['company'])

            given_data = {
                'Inches' : inches,
                'Ram' : ram,
                'Weight' : weight,
                'Screen_width' : screen_width,
                'Screen_height' : screen_height,
                'Frequency' : frequency,
                'Memory_size' : memory_size,
                'Company' : company
            }

            data_df = pd.DataFrame([given_data])

            scaled_data = scaler.transform(data_df)
            prediction = model.predict(scaled_data)

            return render_template('index.html', prediction = f'{prediction[0]:.2f}')

        except Exception as e :
            return render_template('index.html', prediction = f"Error : {str(e)}")

    return render_template('index.html')

if __name__ == '__main__' :
    app.run(debug = True, port = 8000)